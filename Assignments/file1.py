fname = raw_input("Enter file name :")
print fname
try:
        fhand = open(fname)
except:
        print "File not found"
        exit()

for line in fhand:
        line = line.rstrip()
        print line.upper()
