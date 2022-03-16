import re

INTEGER_REGEX = "\d+"

fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "regex_sum_1511080.txt"
file = open(fname)

total = 0


for line in file:
  line = line.rstrip()
  raw_ints = re.findall(string=line, pattern=INTEGER_REGEX)
  for raw_int in raw_ints:
    try:
      number = int(raw_int)
    except:
      continue
    total += number

print(total)
