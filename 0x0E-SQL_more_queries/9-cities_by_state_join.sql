--script that lists all cities contained in the database
SELECT ct.id, ct.name, st.name FROM cities AS ct INNER JOIN states AS st ON st.id=ct.state_id ORDER BY ct.id ASC;
