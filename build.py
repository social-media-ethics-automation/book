import os
import sys
import shutil
import glob
from colorama import Fore



platforms = ["reddit", "discord"]
book_directory = "book_contents"


toc_source = open(book_directory + '/_toc_source.yml', "r").read().split("\n")


for platform in platforms:

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("platform" + platform)
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
        platform_filename = book_directory + "/" + filename.replace("***", platform)
        destination_filename = book_directory + "/" + filename.replace("-***", "")
        
        # figure out file extensions!
        matching_files = [f for f in glob.glob(platform_filename + ".*")]

        file_extension = ""
        if(len(matching_files) == 1):
            file_extension = matching_files[0].split(".")[1]
        else:
            print(Fore.RED + 'Problem: found ' + len(matching_files) + 'files when looking for ' + platform_filename)

        shutil.copy(platform_filename + "." + file_extension, destination_filename + "." + file_extension)

    with open(book_directory + '/_toc.yml', 'w') as file:
        file.write("\n".join(new_toc))

    #print("\n".join(new_toc))


    build_path = "_build/" + platform

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
    shutil.copytree("_build/"+platform+"/_build/html", "docs/"+platform + "/")

# make default forwarding in index.html
with open('docs/index.html', 'w') as file:
    file.write('<meta http-equiv="Refresh" content="0; url='+platforms[0]+'/intro.html" />')

