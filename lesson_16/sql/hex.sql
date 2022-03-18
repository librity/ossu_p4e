CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Annalise', 14);
INSERT INTO Ages (name, age) VALUES ('Seze', 21);
INSERT INTO Ages (name, age) VALUES ('Miah', 32);
INSERT INTO Ages (name, age) VALUES ('Jillianne', 13);
INSERT INTO Ages (name, age) VALUES ('Aylesha', 35);
INSERT INTO Ages (name, age) VALUES ('Fergus', 37);

SELECT hex(name || age) AS X FROM Ages ORDER BY X;
