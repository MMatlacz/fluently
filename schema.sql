drop table if exists culture;
create table culture (
  id integer primary key autoincrement,
  country VARCHAR(255),
  text VARCHAR(255),
  image VARCHAR(255)
);