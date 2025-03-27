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
VALUES ('Tyler Okonma', 'Tyler, The Creator');

INSERT INTO musician (fullname, nickname)
VALUES ('Jacques Webster II', 'Travis Scott');


CREATE TABLE IF NOT EXISTS genre (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL
);



CREATE TABLE IF NOT EXISTS album (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    release_date DATE NOT NULL CHECK (release_date >= '2000-01-01')
);



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


