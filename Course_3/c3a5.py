# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def OpenURL(url, pos, ctx):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        tag = tags[pos - 1]
        return tag.get('href', None), tag.contents[0]

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
count = int(input('Enter count : '))
pos = int(input('Enter position : '))
list_of_names = []
i = 0
while i < count:
        nexturl, name = OpenURL(url, pos, ctx)
        i = i + 1
        url = nexturl
        list_of_names.append(name)

print(list_of_names)
