INSERT INTO files (name, file_type, size, created, modified, location)
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id;