
-- Task 2: Database Interaction

-- 1) Create a MySQL database named 'users'
CREATE DATABASE IF NOT EXISTS users;
USE users;

-- 2) Create the 'users' table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  role VARCHAR(100) NOT NULL
);

-- 3a) Insert sample data
INSERT INTO users (name, email, role) VALUES
('Piyush Mishra', 'piyush@example.com', 'Admin'),
('Vashu Mishra', 'vashu@example.com', 'Editor'),
('Priyam Mishra', 'priyam@example.com', 'Viewer');

-- 3b) Retrieve all users
-- SELECT id, name, email, role FROM users;

-- 3c) Retrieve specific user by ID (example: id = 1)
-- SELECT id, name, email, role FROM users WHERE id = 1;
