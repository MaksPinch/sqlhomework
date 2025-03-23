CREATE TABLE IF NOT EXISTS musician (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    nickname VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS genre (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS genremusician (
    musician_id INTEGER REFERENCES musician(id),
    genre_id INTEGER REFERENCES genre(id),
    CONSTRAINT genremusician_pkey PRIMARY KEY (musician_id, genre_id)
);

CREATE TABLE IF NOT EXISTS album (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    release_date DATE NOT NULL CHECK (release_date >= '2000-01-01')
);

CREATE TABLE IF NOT EXISTS albummusician (
    album_id INTEGER REFERENCES album(id),
    musician_id INTEGER REFERENCES musician(id),
    CONSTRAINT albummusician_pkey PRIMARY KEY (album_id, musician_id)
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

CREATE TABLE IF NOT EXISTS trackcompilation (
    musictrack_id INTEGER REFERENCES musictrack(id),
    compilation_id INTEGER REFERENCES compilation(id),
    CONSTRAINT trackcompilation_pkey PRIMARY KEY (musictrack_id, compilation_id)
);
