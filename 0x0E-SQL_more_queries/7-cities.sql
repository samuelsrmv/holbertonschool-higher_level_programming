-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT,
    state_id INT,
    name VARCHAR(256),
    PRIMARY KEY(id),
    FOREIGN KEY (states.id) REFERENCES hbtn_0d_usa.states(id)
);
