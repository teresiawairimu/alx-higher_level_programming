-- Lists all records of the table
-- Don't list rows without a name value
-- Results should display by the score and the name
-- Records should be listed by descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
