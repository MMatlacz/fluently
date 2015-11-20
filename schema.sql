DROP TABLE if EXISTS entries;
CREATE TABLE phrases (
  id INTEGER PRIMARY KEY autoincrement,
  priority INTEGER,
  english VARCHAR(255),
  polish VARCHAR(255),
  category VARCHAR(255) NOT NULL
);