import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
db = conn.cursor()


db.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if (len(fname) < 1):
  fname = 'library.xml'


def lookup(d, key):
  found = False
  for child in d:
    if found:
      return child.text
    if child.tag == 'key' and child.text == key:
      found = True
  return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
  if (lookup(entry, 'Track ID') is None):
    continue

  name = lookup(entry, 'Name')
  artist = lookup(entry, 'Artist')
  album = lookup(entry, 'Album')
  genre = lookup(entry, 'Genre')
  count = lookup(entry, 'Play Count')
  rating = lookup(entry, 'Rating')
  length = lookup(entry, 'Total Time')

  if name is None:
    continue
  if artist is None:
    continue
  if genre is None:
    continue
  if album is None:
    continue

  print(f"{name} | {artist} | {genre} | {album} | {count} | {rating} | {length}")

  db.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist, ))
  db.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
  artist_id = db.fetchone()[0]

  db.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre, ))
  db.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
  genre_id = db.fetchone()[0]

  db.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
  db.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
  album_id = db.fetchone()[0]

  db.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
             (name, album_id, genre_id, length, rating, count))
conn.commit()


print("\n========== QUERY ==========")
sqlstr = '''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
'''
for row in db.execute(sqlstr):
  print(f"{row[0]} | {row[1]} | {row[2]}")
db.close()
