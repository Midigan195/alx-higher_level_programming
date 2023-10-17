-- Disaply the scores and names of records without a name and in decending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
