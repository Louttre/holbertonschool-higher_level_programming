SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS name
FROM cities
ORDER BY cities.id ASC;
