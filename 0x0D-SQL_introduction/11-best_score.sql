-- Display a list of all the records inside second table with a score >= 10
SELECT score, name
FROM second_table
WHERE (score >= 10)
ORDER BY score DESC;
