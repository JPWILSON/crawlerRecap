import urllib.request
import os


#contents = urllib.request.urlopen('a.html', ).read()

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname('a.html')))

print(__location__)
