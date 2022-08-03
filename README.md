# Social Media, Ethics, and Computer Programming (project page)

This is the project page for the e-book: Social Media, Ethics, and Computer Programming

You can use this site to download a copy of the source of the book and modify it yourself.

## Download the book source code:
Press the green "Code" button on github.

If you want to just download a copy, you can choose the zip file.

If you want to contribute, you'll need to use "git" a version control system that helps track and merge changes:
- Install git (https://git-scm.com/downloads)
- Then open a command line program
  - on Windows: "PowerShell" or "git bash"
  - on Mac: "terminal"
- Navigate using "cd" commands to the place where you want to download the project ([learn more about the terminal](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line))
- enter the command "git clone [url]" where instead of [url], it is the url in that menu opened with the green "Code" button. Something like "https://github.com/kylethayer"
  - Note: you may have to log into github with a special "personal access token" password you'll have to create for your account ([instructions here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))

You should now have a copy of the code on your computer!

If you are going to use git, you can learn more about how to use it on the command line with one of many online tutorials:
- https://www.freecodecamp.org/news/git-and-github-for-beginners/
- https://www.w3schools.com/git/default.asp?remote=github

I also recommend downloading a program that helps you interact with git using a more friendly Graphical User interface, like sourcetree. Then you can open the project folder with sourcetree and view change history and commit your own changes more easily.
- https://www.sourcetreeapp.com/

## Viewing the source code for the book
Once you've downloaded the book source code on your computer, you can go open the various folders and files in the project to see what is in them.

- For most of the files (except the Jupyter Notebook files), you should be able to open them with any text editor.
  - I prefer the program Atom (https://atom.io/). I open the folder of the book project. Then when I'm looking at one of the "md" files I can do top-menu -> packages -> Markdown Preview -> toggle preview, to see how the formatted file looks.

Important files:
- _toc.yml
  - this file is the Table of Contents file, and it lists what all files to load for the book, and how they are organized.
  - If you are creating new section files, or renaming them, or moving them, you'll have to make sure this file is updated to match that.
  - learn more here: https://jupyterbook.org/en/stable/structure/toc.html
- "md" files
  - These are "Markdown" files, which content contents for various sections of the book, using a special set of ways of indicating text formatting.
  - Read more about markdown here: https://www.markdownguide.org/basic-syntax/
  - If you have a program like Atom, you can preview the formatted version of the book section
  - One extra note about markdown: Images are by default just scaled to whatever size they are. So I try to scale images so they display the size I want. For inline images, like in the ethics section, I tried to make them a 4x3 ratio when I could and made them 50x37 pixels, though if they weren't 4x3, I kept the max height at 37.
- Jupter Notebook files (ipynb files)
  - These files can hold both executable code, and text. They are not easily viewable with other text editors.
  - To view Jupyter Notebook files (ipynb files), do the following:
    - Install python (https://www.python.org/downloads/)
    - Install jupyterlab by opening your command line (e.g. PowerShell on Windows, terminal on mac), and entering the command:
      - pip install jupyterlab
    - Then change directory to the directory of the book project (using "cd" commands) and enter the command:
      - jupyter-lab
    - then a browser tab should open to the website http://localhost:8888/, where you should see the JupyterLab editor, and you'll be able to view, run, and modify the ipynb files.

Note: You can also try viewing and editing all files, including jupyter notebook files with Microsoft's Visual Studio Code: https://code.visualstudio.com/

## Building the book (turning source code into website code)

Once you've made changes, you'll probably want to rebuild the website version so you can see how it looks!

To build the website version, first you'll have to have some stuff installed:
- Install python (https://www.python.org/downloads/)
- Install jupyter-book by opening your command line (e.g. PowerShell on Windows, terminal on mac), and entering the command:
  - pip install -U jupyter-book  


To build the book:
- Opening your command line, and change directory to the directory of the book project (using "cd" commands)
- run the following command:
  - jupyter-book build book_contents
- Note: sometimes changes aren't picked up completely, like updated versions of images, so you might need to run clean first to delete the old version of the build:
  - jupyter-book clean book_contents

Once the book is built, then open your finder or file explorer, find the book project code, and the "book_contents" folder inside of that, and the "_build" folder inside of that, and the "html" folder inside of that. Then you should be able to double click on "index.html" to open it in your web browser and view your copy of the ebook webpage files.
