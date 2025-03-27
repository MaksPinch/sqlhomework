CREATE TABLE IF NOT EXISTS musician (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    nickname VARCHAR(40) UNIQUE NOT NULL
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
    title VARCHAR(40) NOT NULL
);

INSERT INTO genre (title)
VALUES ('Hip-Hop');

INSERT INTO genre (title)
VALUES ('Rock');

INSERT INTO genre (title)
VALUES ('Jazz');


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
VALUES ('God\'s Plan', 3.30, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('In My Feelings', 3.95, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Nonstop', 3.20, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Nice for What', 3.65, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Mob Ties', 3.22, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('I\'m Upset', 3.32, 1);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Baby Pluto', 2.90, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Silly Watch', 2.88, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Lo Mein', 2.88, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('That Way', 2.83, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('P2', 3.28, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('You Better Move', 3.05, 2);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Blackstar', 8.00, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Lazarus', 4.78, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Sue (Or in a Season of Crime)', 4.82, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Girl Loves Me', 3.53, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('Dollar Days', 3.47, 3);

INSERT INTO musictrack (title, duration, album_id)
VALUES ('I Can\'t Give Everything Away', 4.18, 3);



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
where duration = (SELECT MAX(duration) FROM musictrack);

SELECT title FROM musictrack
WHERE duration >= 3.5;

SELECT title FROM compilation
WHERE release_date BETWEEN '2018-01-01' AND '2020-12-31';

SELLECT fullname FROM mucisian
WHERE fullname NOT LIKE '% %';

SELECT title FROM musictrack
WHERE title LIKE 'мой' OR title LIKE'my';

# задание 3

SELECT g.title, COUNT(mg.musician_id) FROM genre g
JOIN musician_genre mg ON g.id = mg.genre_id
GROUP BY g.title;

SELECT a.title AS name_of_the_album, a.release_date, COUNT(m.title) AS number_of_tracks
FROM album a
JOIN musictrack m ON a.id = m.album_id
WHERE a.release_date BETWEEN '2019-01-01' AND '2022-12-31'
GROUP BY a.title, a.release_date;


SELECT a.title AS name_of_the_album, AVG(m.duration) AS average_duration FROM album a
JOIN musictrack m ON a.id = m.album_id
GROUP BY a.title;

