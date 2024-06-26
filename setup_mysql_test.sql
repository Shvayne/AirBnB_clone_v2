-- prepares a MYSQL server for the project

-- create the database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the first user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all priviledges of the database to the hbnb_test user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant select privilege on performance_schema to the hbnb_test user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Refresh priviledges
FLUSH PRIVILEGES;