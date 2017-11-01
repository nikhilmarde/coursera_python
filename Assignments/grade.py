score = raw_input("Enter Score: ")
try:
        s = float(score)
except:
        print "Enter numbers between 0.0 and 1.0"
        quit()

if s < 0.0:
        print "Enter numbers greater than 0"
elif s > 1:
        print "Enter numbers between 0.0 and 1.0"
elif s >= 0.9:
        print "A"
elif s >= 0.8:
        print "B"
elif s >= 0.7:
        print "C"
elif s >= 0.6:
        print "D"
else:
        print "F"
