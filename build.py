import os
import sys
 
if "--clean" in sys.argv:
    os.system('jupyter-book clean book_contents')

os.system('jupyter-book build book_contents')