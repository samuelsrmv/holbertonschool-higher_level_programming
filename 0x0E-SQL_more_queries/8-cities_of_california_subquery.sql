-- ists all the cities of California that can be found
SELECT * FROM cities WHERE cities.state_id=(SELECT states.id FROM states WHERE states.name="California") ORDER BY cities.id ASC;
