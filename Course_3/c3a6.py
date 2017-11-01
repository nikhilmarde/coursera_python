import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL : ")
count = 0

xml = ET.fromstring(urllib.request.urlopen(url).read())
lst = xml.findall('comments/comment')
for item in lst:
        count = count + int(item.find('count').text)

print("Total is ", count)
