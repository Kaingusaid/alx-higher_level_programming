-- Say my name
-- A script that lists all records of the table second_table of the database in your MySQL server
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
