from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_33816.html'
html = urlopen(url, context=ctx).read()
tot = 0

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
        # Look at the parts of a tag
        print('TAG:', tag)
        print('Contents:', tag.contents[0])
        tot = tot + int(tag.contents[0])

print(tot)
