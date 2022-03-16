fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "mbox-short.txt"
file = open(fname)

emails = dict()


def handle_line(line):
  tokens = line.split(' ')
  email = tokens[1]
  previous = emails.get(email, 0)
  emails[email] = previous + 1


for line in file:
  if (line.startswith("From:")):
    continue
  if (not line.startswith("From")):
    continue
  line = line.rstrip()
  handle_line(line)


max_email = max(emails, key=emails.get)
max_count = emails[max_email]
print(max_email, max_count)
