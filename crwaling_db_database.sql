CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS data_storage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_type ENUM('json', 'html', 'markdown') NOT NULL,
    content LONGTEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
