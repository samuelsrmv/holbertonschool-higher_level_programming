-- script that creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT SERIAL PRIMARY KEY, name VARCHAR(256),UNIQUE (id));