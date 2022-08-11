-- Select the best
-- A script that lists all records with a score >= 10 in tyhe table of the database in MySQL server
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
