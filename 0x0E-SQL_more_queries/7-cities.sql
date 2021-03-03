-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT FOREIGN (states.id) KEY REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256), 
    UNIQUE (id)
);
