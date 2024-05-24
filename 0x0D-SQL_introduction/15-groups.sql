-- Lists the number of records with the same score in the table
-- The result should display score and number of records of this score
-- List should be sorted by the number of records(descending)
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
