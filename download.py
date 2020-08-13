import sys 
import os
sys.path.append(os.path.abspath("/Users/vlafed/Desktop/work/learning/python/stdlib-python"))

import stdio
import urllib.request

# Accept a name as a command-line argument. Write a message containing
# that name to standard output.

url=sys.argv[1]
fileName=sys.argv[2]

stdio.write("Downloading: " + url)
stdio.write("Saving: " + fileName)

urllib.request.urlretrieve (url, fileName)