import os
import sys
import shutil
import glob
from colorama import Fore



platforms = [
    {"full_name": "Reddit", "file_name": "reddit"},
    {"full_name": "Discord", "file_name": "discord"}
]

# make function for creating social media list
def make_social_media_links(platform, destination_filename):
    # figure out path to updated version of file
    path_parts = destination_filename.split("/")
    path_parts.pop(0) # get rid of the book_contents directory

    # create markdown list of social media sites
    platform_selector = "_Choose Social Media Platform: "

    platform_selector_options = []
    for target_platform in platforms:
        if target_platform == platform:
            platform_selector_options.append("__" + target_platform["full_name"] + "__")
        else:
            #  ../ for as many times as after the index, then new platform, then all the parts after the index
            relative_path = "../" * len(path_parts) + target_platform["file_name"] + "/" + "/".join(path_parts) + ".html"

            platform_selector_options.append("<a href='"+relative_path+"'>"+target_platform["full_name"]+"</a>" )

    platform_selector += " | ".join(platform_selector_options)
    platform_selector += "_"

    return platform_selector

book_directory = "book_contents"


toc_source = open(book_directory + '/_toc_source.yml', "r").read().split("\n")
config_source = open(book_directory + '/_config_source.yml', "r").read().split("\n")


# make new docs
if not os.path.exists("docs"):
    os.mkdir("docs")


for platform in platforms:

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("platform: " + platform["full_name"])
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    

    # Copy over Table of Contents and fix it for the specific platform
    new_toc = toc_source.copy()

    platform_specific_files = []
    for i, toc_line in enumerate(new_toc):

        if(toc_line.endswith("***")):
            platform_specific_files.append(
                toc_line.split(": ")[1]
            )
            new_toc[i] = toc_line.replace("-***", "")


    for filename in platform_specific_files:
        platform_filename = book_directory + "/" + filename.replace("***", platform["file_name"])
        destination_filename = book_directory + "/" + filename.replace("-***", "")
        
        # figure out file extensions!
        matching_files = [f for f in glob.glob(platform_filename + ".*")]

        file_extension = ""
        if(len(matching_files) == 1):
            file_extension = matching_files[0].split(".")[1]
        else:
            print(Fore.RED + 'Problem: found ' + len(matching_files) + 'files when looking for ' + platform_filename)

        #Copy file but add links to other versions
        original_file_location = platform_filename + "." + file_extension
        destination_file_location =  destination_filename + "." + file_extension
        
        file_contents = open(original_file_location, "r").read().split("\n")

        platform_selector = make_social_media_links(platform, destination_filename)
        if(file_extension == "ipynb"):
            # WARNING: This is very brittle coding to find the right place to put the new code

            # Find end of first cell
            end_cell_index = file_contents.index("  },")
            # Add a 
            file_contents.insert(end_cell_index + 1,
            """
              {
                "cell_type": "markdown",
                "id": "123456789-930485093240532940945-0324095320945904325",
                "metadata": {
                    "tags": []
                },
                "source": [" """ + platform_selector +
                """ "]
                },
                """ )
        else: #probably md
            file_contents.insert(1, platform_selector + "\n")
        

        with open(destination_file_location, 'w') as file:
            file.write("\n".join(file_contents))

    with open(book_directory + '/_toc.yml', 'w') as file:
        file.write("\n".join(new_toc))

    # Copy over Table of Contents and fix it for the specific platform
    new_config = config_source.copy()
    for i, config_line in enumerate(new_config):
        if "path_to_book:" in config_line:
            line_parts = config_line.split(":")
            new_config[i] = line_parts[0] + ": " + "docs/"+platform["file_name"] + "/_sources" + " # Optional path to your book, relative to the repository root"

    with open(book_directory + '/_config.yml', 'w') as file:
        file.write("\n".join(new_config))
    
    # Build the project

    build_path = "_build/" + platform["file_name"]

    if "--clean" in sys.argv or "clean" in sys.argv:
        if os.path.exists(build_path) and os.path.isdir(build_path):
            shutil.rmtree(build_path)

    os.system('jupyter-book build book_contents --path-output ' + build_path)

    #Copy files all over to the docs directory

    # first clear old docs
    if os.path.exists("docs/"+platform["file_name"]) and os.path.isdir("docs/"+platform["file_name"]):
        shutil.rmtree("docs/"+platform["file_name"])

    # copy website each platform
    shutil.copytree("_build/"+platform["file_name"]+"/_build/html", "docs/"+platform["file_name"] + "/")

    # copy source docs (so github links and code editor links work correctly)
    # Maybe not needed?
    shutil.copytree("book_contents", "docs/"+platform["file_name"] + "/_sources", dirs_exist_ok = True)


    # Clean up
    os.remove(book_directory + '/_toc.yml')
    os.remove(book_directory + '/_config.yml')

    for filename in platform_specific_files:
        destination_filename = book_directory + "/" + filename.replace("-***", "")
        for f in glob.glob(destination_filename + ".*"):
            os.remove(f)


# make docs version of site


# make default forwarding in index.html
with open('docs/index.html', 'w') as file:
    file.write('<meta http-equiv="Refresh" content="0; url='+platforms[0]["file_name"]+'/intro.html" />')

# github by default uses jekyll, which doesn't work with _ folders
with open('docs/.nojekyll', 'w') as file:
    file.write('')

