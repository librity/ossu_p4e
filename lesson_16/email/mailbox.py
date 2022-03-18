import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
db = conn.cursor()

db.execute('DROP TABLE IF EXISTS Counts')
db.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1):
  fname = 'mbox.txt'
file = open(fname)


def extract_org(line):
  pieces = line.split()
  email = pieces[1]
  pieces = email.split("@")
  org = pieces[1]

  return org


for line in file:
  if not line.startswith('From: '):
    continue

  org = extract_org(line)
  db.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
  row = db.fetchone()

  if row is None:
    db.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
  else:
    db.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
# Commiting outside the loop speeds up the script
conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in db.execute(sqlstr):
  print(str(row[0]), row[1])

db.close()
