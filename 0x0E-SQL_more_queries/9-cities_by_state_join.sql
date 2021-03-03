--script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa; 
INNER JOIN cities ON states.id=cities.state_id