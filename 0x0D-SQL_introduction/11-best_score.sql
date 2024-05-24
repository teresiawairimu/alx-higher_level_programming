-- Lists all records with a score >= 10
-- Results ahould display both score and name
-- Records ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
