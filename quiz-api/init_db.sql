-- SQLite
DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
  id integer PRIMARY KEY,
  position integer,
  title varchar(255),
  text varchar(255),
  image TEXT
);

DROP TABLE IF EXISTS possible_answers;
CREATE TABLE possible_answers (
  id integer PRIMARY KEY,
  question_id integer,
  text varchar(255),
  is_correct bool,
  FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS participations;
CREATE TABLE participations (
  id integer PRIMARY KEY,
  nom varchar(255),
  score int
);

DROP TABLE IF EXISTS admins;
CREATE TABLE admins (
  id integer PRIMARY KEY AUTOINCREMENT,
  username varchar(255) UNIQUE,
  password varchar(255)
);

INSERT INTO admins(username,password) VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3');