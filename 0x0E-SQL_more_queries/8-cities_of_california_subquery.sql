-- ists all the cities of California that can be found
SELECT * FROM cities WHERE state_id=(SELECT id FROM states WHERE states.name="California") ORDER BY cities.id ASC;
