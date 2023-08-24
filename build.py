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
def make_social_media_links(platform, destination_file_location):
    # TODO: also need path to udpate path
    platform_selector = "_Choose Social Media Platform: "

    platform_selector_options = []
    for target_platform in platforms:
        if target_platform == platform:
            platform_selector_options.append("__" + target_platform["full_name"] + "__")
        else:
            platform_selector_options.append("[" + target_platform["full_name"] + "]("+ "" + ")" )

    platform_selector += " | ".join(platform_selector_options)
    platform_selector += "_"

    return platform_selector

book_directory = "book_contents"


toc_source = open(book_directory + '/_toc_source.yml', "r").read().split("\n")




for platform in platforms:

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("platform: " + platform["full_name"])
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    

    new_toc = toc_source.copy()

    platform_specific_files = []
    for i, toc_line in enumerate(new_toc):

        if(toc_line.endswith("***")):
            platform_specific_files.append(
                toc_line.split(": ")[1]
            )
            new_toc[i] = toc_line.replace("-***", "")
            print("updated: " + new_toc[i])


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

        platform_selector = make_social_media_links(platform, destination_file_location)
        file_contents.insert(1, platform_selector + "\n")

        with open(destination_file_location, 'w') as file:
            file.write("\n".join(file_contents))

    with open(book_directory + '/_toc.yml', 'w') as file:
        file.write("\n".join(new_toc))

    #print("\n".join(new_toc))


    build_path = "_build/" + platform["file_name"]

    if "--clean" in sys.argv:
        os.system('jupyter-book clean book_contents --path-output ' + build_path)

    os.system('jupyter-book build book_contents --path-output ' + build_path)

    os.remove(book_directory + '/_toc.yml')

    for filename in platform_specific_files:
        destination_filename = book_directory + "/" + filename.replace("-***", "")
        for f in glob.glob(destination_filename + ".*"):
            os.remove(f)


# make docs version of site

# clear old docs
if os.path.exists("docs") and os.path.isdir("docs"):
    shutil.rmtree("docs/")

# make new docs
os.mkdir("docs")


# copy each platform
for platform in platforms:
    shutil.copytree("_build/"+platform["file_name"]+"/_build/html", "docs/"+platform["file_name"] + "/")

# make default forwarding in index.html
with open('docs/index.html', 'w') as file:
    file.write('<meta http-equiv="Refresh" content="0; url='+platforms[0]["file_name"]+'/intro.html" />')

# github by default uses jekyll, which doesn't work with _ folders
with open('docs/.nojekyll', 'w') as file:
    file.write('')

