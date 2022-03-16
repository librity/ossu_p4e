fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "mbox-short.txt"
file = open(fname)

hours = dict()


def handle_line(line):
  tokens = line.split(' ')
  time = tokens[6]
  hour = time.split(':')[0]

  previous = hours.get(hour, 0)
  hours[hour] = previous + 1


for line in file:
  if (not line.startswith("From ")):
    continue
  line = line.rstrip()
  handle_line(line)


hours_l = list()
for hour, count in hours.items():
  hours_l.append((hour, count))
hours_l.sort()


for hour, count in hours_l:
  print(hour, count)
