fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "mbox-short.txt"

fh = open(fname)
count = 0


def handle_line(line):
  tokens = line.split(' ')
  print(tokens[1])
  count += 1


for line in fh:
  if (line.startswith("From:")):
    continue
  if (not line.startswith("From")):
    continue
  handle_line(line)

print("There were", count, "lines in the file with From as the first word")
