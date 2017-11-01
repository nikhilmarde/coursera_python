# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
        fh = open(fname)
except:
        print "File not found", fname

numlines = 0
avg_spam_conf = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : 
                continue

        line = line.rstrip()
        numlines += 1
        startpos = line.find(":") + 1
        avg_spam_conf = avg_spam_conf + float(line[startpos:].strip())

if numlines > 0:
        print "Average spam confidence:", avg_spam_conf/numlines
