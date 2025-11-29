INSERT INTO files (name, file_type, size, created, modified, location)
VALUES (%s, %s, %s, COALESCE(%s, NOW()), COALESCE(%s, NOW()), COALESCE(%s, ''))
RETURNING id;