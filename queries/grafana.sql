-- average file size by ile type
SELECT
  file_type,
  AVG(size) AS avg_file_size
FROM
  files
GROUP BY
  file_type
ORDER BY
  avg_file_size DESC

-- file type distribution
SELECT
  file_type,
  COUNT(id) AS file_count
FROM
  files
GROUP BY
  file_type
ORDER BY
  file_count DESC

-- file count over time
SELECT
  $__timeGroup(created, '1d') AS time,
  COUNT(id) AS file_count
FROM
  files
GROUP BY
  time
ORDER BY
  time

-- file size growth over time
SELECT
  $__timeGroup(created, '1d') AS time,
  SUM(size) AS total_file_size
FROM
  files
GROUP BY
  time
ORDER BY
  time
