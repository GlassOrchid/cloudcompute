CREATE TABLE files (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    size BIGINT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT NOW(),
    modified TIMESTAMP NOT NULL DEFAULT NOW(),
    location TEXT NOT NULL
);


INSERT INTO files (name, size, created, modified, location)
VALUES ('example.txt', 2048, NOW(), NOW(), '/usr/local/files/');

SELECT * FROM files;

