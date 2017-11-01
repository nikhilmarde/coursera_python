import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = input("Enter URL : ")
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read().decode()
#print("data : ", data)

info = json.loads(data)
print('User count:', info)

for item in info['comments']:
#    print(item)
    count = count + int(item['count'])

print("total : ", count)
"""
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
"""
