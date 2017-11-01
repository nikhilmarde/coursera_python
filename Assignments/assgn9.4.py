"""
9.4 Write a program to read through the mbox-short.txt and figure out who 
has the sent the greatest number of mail messages. The program looks for 
'From ' lines and takes the second word of those lines as the person who 
sent the mail. The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer.
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
        fname = "mbox-short.txt"

fh = open(fname)

count = 0
newdict = dict()
for line in fh:
        line = line.rstrip()
        if not line.startswith("From "):
                continue

        count += 1
        spltline = line.split()
        email_add = spltline[1]
        newdict[email_add] = newdict.get(email_add, 0) + 1

max_email = None
max_count = None

for key,value in newdict.items():
        if max_email is None or value > max_count :
                max_email = key
                max_count = value

print max_email, max_count
