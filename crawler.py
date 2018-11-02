import urllib.request
import os


#contents = urllib.request.urlopen('a.html', ).read()

#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('a.html')))
file_one = "a.html"

content = []
with open(file_one, "rb") as f:
    s = f.read()
    content.append(s)

print(content)
