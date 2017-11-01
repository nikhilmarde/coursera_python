hrs = raw_input("Enter Hours:")
try:
        h = float(hrs)
except:
        print "Please enter a valid number"
        exit

rate = raw_input("Enter Rate:")
try:
        r = float(rate)
except:
        print "Please enter a valid number"
        exit

if h <= 40:
        pay = h * r
else:
        pay = (40 * r) + ((h - 40) * (r * 1.5))

print pay
