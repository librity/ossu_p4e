lst = list()
fname = input("Enter file name: ")
fh = open(fname)


def add_words(words):
  for word in words:
    if (word not in lst):
      lst.append(word)


for line in fh:
  line = line.rstrip()
  words = line.split(' ')
  add_words(words)


lst.sort()
print(lst)
