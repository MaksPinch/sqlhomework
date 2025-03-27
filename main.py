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

INSERT INTO musictrack (title, duration, album_id)
VALUES ('God\'s Plan', 198, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('In My Feelings', 237, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Nonstop', 192, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Nice for What', 219, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Mob Ties', 193, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('I\'m Upset', 199, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Baby Pluto', 174, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Silly Watch', 173, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Lo Mein', 173, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('That Way', 170, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('P2', 197, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('You Better Move', 183, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Blackstar', 480, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Lazarus', 287, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Sue (Or in a Season of Crime)', 289, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Girl Loves Me', 212, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Dollar Days', 208, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('I Can\'t Give Everything Away', 251, 3);

CREATE TABLE IF NOT EXISTS compilation (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20) NOT NULL,
    release_date DATE NOT NULL CHECK (release_date >= '2000-01-01')
);

INSERT INTO compilation (title, release_date)
VALUES ('The Best of Drake', '2020-01-01');

INSERT INTO compilation (title, release_date)
VALUES ('The Uzi Collection', '2021-05-15');

INSERT INTO compilation (title, release_date)
VALUES ('Miles Davis Essentials', '2017-07-12');

INSERT INTO compilation (title, release_date)
VALUES ('David Bowie Greatest Hits', '2019-09-20');

CREATE TABLE IF NOT EXISTS musician_genre (
    musician_id INTEGER REFERENCES musician(id),
    genre_id INTEGER REFERENCES genre(id),
    PRIMARY KEY (musicain_id, genre_id)
);

INSERT INTO musician_genre (musician_id, genre_id)
VALUES (1, 1);

INSERT INTO musician_genre (musician_id, genre_id)
VALUES (2, 1);

INSERT INTO musician_genre (musician_id, genre_id)
VALUES (3, 3);

INSERT INTO musician_genre (musician_id, genre_id)
VALUES (4, 2);

CREATE TABLE IF NOT EXISTS album_musician (
    album_id INTEGER REFERNCES album(id),
    musicain_id INTEGER REFERNCES musician(id),
    PRIMARY KEY (album_id, musician_id)
);

INSERT INTO album (album_id, musician_id)
VALUES (1,1);

INSERT INTO musician_album (musician_id, album_id)
VALUES (2, 2);

INSERT INTO musician_album (musician_id, album_id)
VALUES (3, 3);

INSERT INTO musician_album (musician_id, album_id)
VALUES (4, 3);