INSERT INTO files (name, size, created, modified, location)
VALUES (%s, %s, NOW(), NOW(), %s)
RETURNING id;
