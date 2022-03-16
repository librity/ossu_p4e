import re

INTEGER_REGEX = "\d+"

file = """
Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
""".split('\n')
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
