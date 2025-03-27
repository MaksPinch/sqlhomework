

CREATE TABLE IF NOT EXISTS musician (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    nickname VARCHAR(100) UNIQUE NOT NULL
);
# задание 1
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
    title VARCHAR(100) NOT NULL
);

INSERT INTO genre (title)
VALUES ('Hip-Hop');

INSERT INTO genre (title)
VALUES ('Rock');

INSERT INTO genre (title)
VALUES ('Jazz');


CREATE TABLE IF NOT EXISTS album (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
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
    title VARCHAR(100) NOT NULL,
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
VALUES ('P2', 196, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('You Better Move', 183, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Blackstar', 480, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Lazarus', 288, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Sue (Or in a Season of Crime)', 289, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Girl Loves Me', 213, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Dollar Days', 208, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('I Can\'t Give Everything Away', 252, 3);




CREATE TABLE IF NOT EXISTS compilation (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
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
    PRIMARY KEY (musician_id, genre_id)
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
    album_id INTEGER REFERENCES album(id),
    musician_id INTEGER REFERENCES musician(id),
    PRIMARY KEY (album_id, musician_id)
);


INSERT INTO album_musician (album_id, musician_id)
VALUES (1, 1);

INSERT INTO album_musician (album_id, musician_id)
VALUES (2, 2);

INSERT INTO album_musician (album_id, musician_id)
VALUES (3, 3);

INSERT INTO album_musician (album_id, musician_id)
VALUES (3, 4);


CREATE TABLE IF NOT EXISTS compilation_track (
    compilation_id INTEGER REFERENCES compilation(id),
    musictrack_id INTEGER REFERENCES musictrack(id),
    PRIMARY KEY (compilation_id, musictrack_id)
);


INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (1, 1);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (1, 2);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (2, 7);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (2, 8);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (3, 13);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (3, 14);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (4, 17);

INSERT INTO compilation_track (compilation_id, musictrack_id)
VALUES (4, 18);

# задание 2

SELECT title, duration FROM musictrack
WHERE duration = (SELECT MAX(duration) FROM musictrack);

SELECT title FROM musictrack
WHERE duration >= 210;

SELECT title FROM compilation
WHERE release_date BETWEEN '2018-01-01' AND '2020-12-31';

SELECT fullname FROM musician
WHERE fullname NOT LIKE '% %';

SELECT title FROM musictrack
WHERE title ILIKE 'my%'
OR title ILIKE '%my'
OR title ILIKE '%my%'
OR title ILIKE 'my'

# задание 3

SELECT g.title, COUNT(mg.musician_id) FROM genre g
JOIN musician_genre mg ON g.id = mg.genre_id
GROUP BY g.title;

SELECT COUNT(*)
FROM musictrack m
JOIN album a ON a.id = m.album_id
WHERE a.release_date BETWEEN '2019-01-01' AND '2022-12-31';


SELECT a.title AS name_of_the_album, AVG(m.duration) AS average_duration FROM album a
JOIN musictrack m ON a.id = m.album_id
GROUP BY a.title;

SELECT fullname
FROM musician
WHERE id NOT IN (
    SELECT fullname as name
    FROM musician m
    JOIN album_musician am ON m.id = am.musician_id
    JOIN album a ON am.album_id = a.id
    WHERE a.release_date BETWEEN '2020-01-01' AND '2020-12-31'
);

SELECT DISTINCT c.title AS name_of_the_compilation
FROM compilation c
JOIN compilation_track ct ON c.id = ct.compilation_id
JOIN musictrack m ON ct.musictrack_id = m.id
JOIN album a ON m.album_id = a.id
JOIN album_musician am ON a.id = am.album_id
JOIN musician ms ON am.musician_id = ms.id
WHERE ms.fullname = 'Drake';

