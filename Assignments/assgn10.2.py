"""
10.2 Write a program to read through the mbox-short.txt and figure out 
the distribution by hour of the day for each of the messages. You can 
pull the hour out from the 'From ' line by finding the time and then 
splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.

Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
        fname = "mbox-short.txt"

fh = open(fname)

newdict = dict()
for line in fh:
        line = line.rstrip()
        if not line.startswith("From "):
                continue

        spltline = line.split()
        time_of_email = spltline[5]
        hour = time_of_email.split(":")
        newdict[hour[0]] = newdict.get(hour[0], 0) + 1

#print newdict.items()
for k,v in sorted(newdict.items()):
        print k, v, "*"*v


"""
max_email = None
max_count = None

for key,value in newdict.items():
        if max_email is None or value > max_count :
                max_email = key
                max_count = value

print max_email, max_count
"""
