-- Script that creates a database and a table
-- Query to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Query to create cities in hbtn_0d    _usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
       state_id INT FOREIGN KEY REFERENCES states(id) NOT NULL,
       name VARCHAR(256) NOT NULL);
