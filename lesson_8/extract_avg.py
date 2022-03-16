def get_float(line):
  f_position = line.find(':')
  number = float(line[f_position+1:])
  return (number)


total = 0.0
count = 0
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  if not line.startswith("X-DSPAM-Confidence:"):
    continue
  total += get_float(line)
  count += 1

avarage = total / count
print("Average spam confidence:", avarage)
