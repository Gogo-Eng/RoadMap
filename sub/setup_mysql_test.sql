-- script that prepares a MySQL server for the project
-- creating a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- setting up password
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- granting privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- granting select privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;