fname = raw_input("Enter file name: ")
try:
        fh = open(fname)
except:
        print "File not found ", fname
        exit()

lst = []
for line in fh:
        line = line.rstrip()
        print "Line is : ", line
        spltline = line.split()
        print "Split line is : ", spltline
        for i in spltline:
                print "i : ", i
                if i in lst:
                        continue

                lst.append(i)

print "list is now : ", lst
lst.sort()
print "sorted list is : ", lst
