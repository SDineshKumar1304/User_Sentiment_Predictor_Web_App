create database SENTIMENT_ANALYSIS;
use  SENTIMENT_ANALYSIS;
drop table users;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone_Number VARCHAR(20) NOT NULL,
    New_Password VARCHAR(255) NOT NULL,
    Confirm_Password VARCHAR(255) NOT NULL
);


select * from users;
show tables;

