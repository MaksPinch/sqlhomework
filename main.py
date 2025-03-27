CREATE TABLE IF NOT EXISTS musician (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    nickname VARCHAR(40) UNIQUE NOT NULL
);

INSERT INTO musician (fullname, nickname)
VALUES ('Aubrey Drake Graham', 'Drake');

INSERT INTO musician (fullname, nickname)
VALUES ('Symere Woods', 'Lil Uzi Vert');

INSERT INTO musician (fullname, nickname)
VALUES ('Miles Dewey Davis III', 'Miles Davis');

INSERT INTO musician (fullname, nickname)
VALUES ('David Robert Jones', 'David Bowie');


CREATE TABLE IF NOT EXISTS genre (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL
);

INSERT INTO genre (title)
VALUES ('Hip-Hop');

INSERT INTO genre (title)
VALUES ('Rock');

INSERT INTO genre (title)
VALUES ('Jazz')

CREATE TABLE IF NOT EXISTS album (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    release_date DATE NOT NULL CHECK (release_date >= '2000-01-01')
);

INSERT INTO album (title, release_date)
VALUES ('Scorpion', '2018-06-29');

INSERT INTO album (title, release_date)
VALUES ('Eternal Atake', '2020-03-06');

INSERT INTO album (title, release_date)
VALUES ('Blackstar', '2016-01-08');

CREATE TABLE IF NOT EXISTS musictrack (
    id SERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    duration INTEGER NOT NULL CHECK (duration > 0),
    album_id INTEGER REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS compilation (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20) NOT NULL,
    release_date DATE NOT NULL CHECK (release_date >= '2000-01-01')
);


