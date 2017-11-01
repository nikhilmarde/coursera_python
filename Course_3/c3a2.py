import re

fname = input("Enter File name to open :")
if len(fname) < 1:
        fname = "regex_sum_42.txt"

fh = open(fname)

num = 0
lst_num = []

for line in fh:
        line = line.strip()
        lst_num = re.findall('[0-9]+', line)
        if len(lst_num) > 0:
                print(lst_num)
                for n in lst_num:
                        num = num + int(n)

print("Total is ", num)
