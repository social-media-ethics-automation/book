# Note: args that it can take: --clean, --pdf

# Note: for Pdf building: need this fix 
# Find pdf.py (using python console): 
#              import jupyter_book.pdf
#              jupyter_book.pdf.__file__
# edit pdf.py library
#     -  await page.goto(f"file:///{html_file}", {"waitUntil": ["networkidle2"]})
#        to
#     -  await page.goto(f"file:///{html_file}", {"timeout": 0, "waitUntil": ["networkidle2"]})
#  - https://github.com/executablebooks/jupyter-book/issues/1732
# also TODO: make depth 0 and do  --builder pdflatex --individualpages for chapter files


# Note: requires sphinxext-opengraph

import os
import sys
import shutil
import glob
from colorama import Fore
from colorama import init
init(autoreset=True)

# Note: status can be something like: " (incomplete)"
platforms = [
   {"full_name": "Bluesky", "file_name": "bsky", "status": ""},
   {"full_name": "Reddit", "file_name": "reddit", "status": ""},
   {"full_name": "Discord", "file_name": "discord", "status": ""},
   {"full_name": "No Coding", "file_name": "nocode", "status": "", "keep_all_files": True, "exclude_from_options": True}, # First pass makes copies of all coding files (so they can be linked to) 
   {"full_name": "No Coding", "file_name": "nocode", "status": "", "keep_all_files": False, "second_pass": True} # Second pass gets rid of some of the coding files (for better flow)
]


############ Helper Function ############################

# make function for creating social media list
def make_social_media_links(platform, destination_filename, include_status = False, isGenericCodeVersion = False):
    # figure out path to updated version of file
    path_parts = destination_filename.split("/")
    path_parts.pop(0) # get rid of the book_contents directory

    # create markdown list of social media sites
    platform_selector = "_Choose Social Media Platform: "
    if isGenericCodeVersion:
        platform_selector = "_If you don't want the coding version of this online textbook go here: "
    

    platform_selector_options = []
    for target_platform in platforms:
        if(not "exclude_from_options" in target_platform and
           not (isGenericCodeVersion and target_platform["file_name"] != "nocode")):
            if target_platform["file_name"] == platform["file_name"]:
                platform_string = target_platform["full_name"]
                if(include_status):
                    platform_string += target_platform["status"]
                platform_selector_options.append("__" + platform_string + "__")
            else:
                #  ../ for as many times as after the index, then new platform, then all the parts after the index
                relative_path = "../" * len(path_parts) + target_platform["file_name"] + "/" + "/".join(path_parts) + ".html"
                
                platform_string = target_platform["full_name"]
                if(include_status):
                    platform_string += target_platform["status"]
                
                platform_selector_options.append("<a href='"+relative_path+"'>"+platform_string+"</a>" )

    platform_selector += " | ".join(platform_selector_options)
    platform_selector += "_"

    return platform_selector


# try to find specific version file, if not version and not nocode, try to find "code" version
# Returns matching files array (if any matched), the platform_filename, and isGenericCodeVersion 
def find_platform_specific_source_file(filename, platform):
    platform_filename = "no_file_to_be_found"

    # try to find specific version file, if not version and not nocode, try to find "code" version
    if(platform["file_name"] == "nocode"):
        platform_filename = book_directory + "/" + filename.replace("***", platform["file_name"])
        matching_files = [f for f in glob.glob(platform_filename + ".*")]
        return (matching_files, platform_filename, False)

    else: # one of the code versions
        platform_filename = book_directory + "/" + filename.replace("***", platform["file_name"])
        matching_files = [f for f in glob.glob(platform_filename + ".*")]
        if(len(matching_files) > 0):
            return (matching_files, platform_filename, False)
        
        #if we couldn't find specific code version, try generic "code" version
        platform_filename = book_directory + "/" + filename.replace("***", "code")
        matching_files = [f for f in glob.glob(platform_filename + ".*")]

        if(len(matching_files) > 0): #if we found a generic "code" version, it is return with generic set to true
            return (matching_files, platform_filename, True)
        
        return (matching_files, platform_filename, False)



############ Main Code ############################

book_directory = "book_contents"


toc_source = open(book_directory + '/_toc_source.yml', "r").read().split("\n")
config_source = open(book_directory + '/_config_source.yml', "r").read().split("\n")




# Clean project build if it is a clean build
if "--clean" in sys.argv or "clean" in sys.argv:
    print()
    print("Cleaning project build...")
    print()
    for platform in platforms:
        build_path = "_build/" + platform["file_name"]
        if os.path.exists(build_path) and os.path.isdir(build_path):
            shutil.rmtree(build_path)



# clear old docs directory 
if os.path.exists("docs/") and os.path.isdir("docs/"):
    if "--pdf" in sys.argv:
        shutil.rmtree("docs/") 
    else:  # delete everything but pdfs (since we aren't rebuilding them)
        for root, dirs, files in os.walk("docs/", topdown=False):
            for name in files:
                if(not name.endswith(".pdf")):
                    os.remove(os.path.join(root, name))
            for name in dirs:
                dir = os.listdir(os.path.join(root, name)) 
                if len(dir) == 0: 
                    os.rmdir(os.path.join(root, name))

# make a publish "docs" directory if it doesn't exist yet
if not os.path.exists("docs"):
    os.mkdir("docs")


for platform in platforms:

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("platform: " + platform["full_name"])
    if "keep_all_files" in platform:
        print("keep_all_files: " + str(platform["keep_all_files"]))
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    # if second pass, clear the build directory (to hopefully make new, updated files)
    if("second_pass" in platform and ("--clean" in sys.argv or "clean" in sys.argv) ):
        build_path = "_build/" + platform["file_name"]
        if os.path.exists(build_path) and os.path.isdir(build_path):
            shutil.rmtree(build_path)

    # Copy over Table of Contents and fix it for the specific platform
    new_toc = toc_source.copy()
    
    platform_specific_files = []
    platform_specific_files_to_clean = []

    if(platform["file_name"] == "nocode"):
        for i, toc_line in enumerate(new_toc):
            # make replacement files for ++noprogkeep and ++noprogrem
            if toc_line.endswith("++noprogkeep") or (platform["keep_all_files"] and toc_line.endswith("++noprogremove")):
                toc_line = toc_line.replace("++noprogkeep", "")
                toc_line = toc_line.replace("++noprogremove", "")
                if "sections:" not in toc_line: # don't include "sections:" lines
                    platform_specific_files.append(
                        toc_line.split(": ")[1]
                    )
                toc_line = toc_line.replace("-***", "")
                new_toc[i] = toc_line
            elif toc_line.endswith("++noprogremove"):
                new_toc[i] = ""
            else:
                new_toc[i] = toc_line.replace("-***", "")
        
    else: # it's one of the coding options
        for i, toc_line in enumerate(new_toc):

            # Remove any ++noprogkeep and ++noprogrem
            toc_line = toc_line.replace("++noprogkeep", "")
            toc_line = toc_line.replace("++noprogremove", "")

            # if it is platform specific, 
            if(toc_line.endswith("***")):
                platform_specific_files.append(
                    toc_line.split(": ")[1]
                )
                new_toc[i] = toc_line.replace("-***", "")
            else:
                new_toc[i] = toc_line


    # Fix _intro_source.md
    intro_source = open(book_directory + '/_intro_source.md', "r").read().split("\n")
    platform_selector = make_social_media_links(platform, book_directory + "/intro", include_status=True)

    fix_line = intro_source.index("% TODO: Auto-insert download link and versions")
    intro_source[fix_line] = "There are different versions of this book for making bots in different platforms: \n\n" + platform_selector + "\n" + \
                           "\n" + "You can <a href='./social_media_ethics_automation_"+platform["file_name"]+".pdf'>download this book as a pdf here </a> (though not everything will work correctly or be interactive as a pdf). (Also, if anyone knows how to make jupyterbooks make separate pdfs for each chapter, please let Kyle know.)"

    with open(book_directory + '/intro.md', 'w') as file:
            file.write("\n".join(intro_source))


    # Fix rest of files
    for filename in platform_specific_files:
        if "***" in filename: # only try to fill in filenames where that is requested
            # try to find specific version file, if not version and not nocode, try to find "code" version
            (matching_files, platform_filename, isGenericCodeVersion) = find_platform_specific_source_file(filename, platform)

            destination_filename = book_directory + "/" + filename.replace("-***", "")
            
            # figure out file extensions and get contents
            file_extension = ""
            file_contents = ""
            if(len(matching_files) == 1):
                file_extension = matching_files[0].split(".")[1]

                # Read old file to here
                original_file_location = platform_filename + "." + file_extension

                try:
                    file_contents = open(original_file_location, "r").read()
                except Exception as e:
                    try: 
                        file_contents = open(original_file_location, "r", encoding="utf8").read()
                    except:
                        print(Fore.RED + 'ERROR READING FILE: ' + original_file_location)
                        print(e)
                        continue
                
                file_contents = file_contents.split("\n")

            elif(len(matching_files) == 0):
                

                # find any file for any platform
                any_platform_filename = book_directory + "/" + filename.replace("***", "*")
                any_matching_files = [f for f in glob.glob(any_platform_filename)]

                if(len(any_matching_files) == 0):
                    print(Fore.RED + 'Error: couldn\'t find any file matching ' + any_platform_filename + ', so can\'t make a stub version.')
                    continue


                # read contents of first open file
                file_to_get_title_from = any_matching_files[0]
                print(Fore.RED + 'Warning: couldn\'t find ' + platform_filename + '. Making a stub file from:' + file_to_get_title_from)
                
                file_to_get_title_from_contents = open(file_to_get_title_from, "r", encoding='cp437').read().split("\n")
                
                file_to_get_title_from_extension = file_to_get_title_from.split(".")[1]
                title_text = ""
                # WARNING: Finding Titles is brittle code
                if(file_to_get_title_from_extension == "ipynb"): #Try to find the title header in the ipynb file
                    title_line = ""
                    for line in file_to_get_title_from_contents:
                        if '"# ' in line:
                            title_line = line
                            break
                    title_line = title_line.strip()
                    if title_line[0] != '"' and title_line[-1] != '"':
                        print(Fore.RED + 'Error: alternate file ' + file_to_get_title_from_extension + '. title line didn\'t work: ' + title_line)
                        continue
                    
                    title_text = title_line[1:-1]

                else: #probably md, title should be first line
                    title_text = file_to_get_title_from_contents[0]
                
                # our new stub file will be an md file with a warning note
                file_extension = "md"
                file_contents = []
                if(platform["file_name"] == "nocode"):
                    file_contents = [title_text, 
                                    "__This section is for coding versions of this book only. If you want to look at code, please select one of the platforms.__"]
                else:
                    file_contents = [title_text, 
                                    "__Content for the social media platform "+ platform["full_name"] +" hasn't been created yet. Please try another platform.__"]

            else:
                print(Fore.RED + 'Problem: found ' + len(matching_files) + 'files when looking for ' + platform_filename)
                continue

            #Make new file (copied from old, if it existed), but with links

            destination_file_location =  destination_filename + "." + file_extension
            
            platform_selector = make_social_media_links(platform, destination_filename, isGenericCodeVersion = isGenericCodeVersion)
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
            
            print("saving file (and marking to be deleted): " + destination_file_location)
            platform_specific_files_to_clean.append(destination_file_location)
            with open(destination_file_location, 'w', encoding="utf8") as file:
                file.write("\n".join(file_contents))

    with open(book_directory + '/_toc.yml', 'w') as file:
        file.write("\n".join(new_toc))

    # Copy over Table of Contents and fix it for the specific platform
    new_config = config_source.copy()
    for i, config_line in enumerate(new_config):
        if "path_to_book:" in config_line:
            line_parts = config_line.split(":")
            new_config[i] = line_parts[0] + ": " + "docs/"+platform["file_name"] + "/_sources" + " # Optional path to your book, relative to the repository root"
        
    # Fix book source code link
    for i, config_line in enumerate(new_config):
        if "  url: https://github.com/social-media-ethics-automation/book/  # TODO Script updates this to platform specific copy" in config_line:
            new_config[i] = "  url: https://github.com/social-media-ethics-automation/book-src-"+platform["file_name"]+"/"


    with open(book_directory + '/_config.yml', 'w') as file:
        file.write("\n".join(new_config))
    
    # Build the project

    build_path = "_build/" + platform["file_name"]


    # If we want pdf, first make single page version of site, then build the pdf, then do normal build
    if "--pdf" in sys.argv and not ("exclude_from_options" in platform and platform["exclude_from_options"] == True):
        os.system('jupyter-book build book_contents --builder pdfhtml --path-output ' + build_path)

    os.system('jupyter-book build book_contents --path-output ' + build_path)

    #Copy files all over to the docs directory

    # copy website each platform
    shutil.copytree("_build/"+platform["file_name"]+"/_build/html", "docs/"+platform["file_name"] + "/", dirs_exist_ok=True)

    #move pdf (if pdf enabled) (It's a big file, so move instead of copy)
    if "--pdf" in sys.argv and not ("exclude_from_options" in platform and platform["exclude_from_options"] == True):
        shutil.move("_build/"+platform["file_name"]+"/_build/pdf/book.pdf", "docs/"+platform["file_name"] + "/social_media_ethics_automation_" + platform["file_name"] + ".pdf")


    # copy source docs (so github links and code editor links work correctly) into module repos
    # NOTE: To add a new submodule repo to hold the source copy run a command like this:
    #  git submodule add -f https://github.com/social-media-ethics-automation/book-src-reddit.git src-copies/book-src-reddit
    shutil.copytree("book_contents", 
                    "src-copies/book-src-"+platform["file_name"], 
                    dirs_exist_ok = True, 
                    ignore=shutil.ignore_patterns('*.pptx', '*.ipynb_checkpoints*'))
    # Make a README for the submodule copy of book source
    with open("src-copies/book-src-"+platform["file_name"] + '/README.md', 'w') as file:
        file.write("# Social Media, Ethics, and Automation - " + platform["full_name"] + " source\n" +
                   "This is a copy of the book source for the "+ platform["full_name"] + " version of the book.\n\n" + 
                   "This copy was created to help make the interactive online code editors work better.\n\n" + 
                   "The original source code is at: https://github.com/social-media-ethics-automation/book")
        
    # copy .gitignore
    shutil.copy(".gitignore", "src-copies/book-src-"+platform["file_name"] + "/.gitignore")


    # Clean up
    os.remove(book_directory + '/_toc.yml')
    os.remove(book_directory + '/_config.yml')
    os.remove(book_directory + '/intro.md')

    for filename in platform_specific_files_to_clean:
        os.remove(filename)


# make docs version of site


# make default forwarding in index.html
with open('docs/index.html', 'w') as file:
    file.write("""<head>
            <meta http-equiv="Refresh" content="0; url={platform}/intro.html" />
            <meta property="og:title" content="Social Media, Ethics, and Automation" />
            <meta property="og:type" content="book" />
            <meta property="og:url" content="intro.html" />
            <meta property="og:site_name" content="Social Media, Ethics, and Automation" />
            <meta property="og:description" content="Free textbook on programming social media bots and considering the ethical implications of having done so. Automation drives our experience of social media platforms, from timeline feeds to disinfo..." />
            <meta property="og:image" content="https://social-media-ethics-automation.github.io/book/{platform}/_images/logo.png" />
            <meta property="og:image:alt" content="Social Media, Ethics, and Automation" />
            <meta name="description" content="Free textbook on programming social media bots and considering the ethical implications of having done so. Automation drives our experience of social media platforms, from timeline feeds to disinfo..." />

            <title>Social Media, Ethics, and Automation &#8212; by Kyle Thayer and Susan Notess</title>
        </head>""".format(platform=platforms[0]["file_name"]))

# make default 404 page that forwards in index.html
with open('docs/404.html', 'w') as file:
    file.write('<meta http-equiv="Refresh" content="0; url=/book/'+platforms[0]["file_name"]+'/intro.html" />')


# github by default uses jekyll, which doesn't work with _ folders
with open('docs/.nojekyll', 'w') as file:
    file.write('')

