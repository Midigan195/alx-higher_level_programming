-- Dispaly all the cities of california
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id;
