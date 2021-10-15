USE waaseteam2 ;

DROP TABLE IF EXISTS waaseteam2.input_data;
DROP TABLE IF EXISTS waaseteam2.data_type;
DROP TABLE IF EXISTS waaseteam2.device;
DROP TABLE IF EXISTS waaseteam2.user;
DROP TABLE IF EXISTS waaseteam2.device_type;


CREATE TABLE user (
ID INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(255),
last_name VARCHAR(255),
email VARCHAR(255),
password VARCHAR(255),
last_updated TIMESTAMP DEFAULT now(),
PRIMARY KEY (ID)
) AUTO_INCREMENT = 0;



CREATE TABLE device_type (
ID INT NOT NULL AUTO_INCREMENT,
model VARCHAR(255),
PRIMARY KEY (ID)
) AUTO_INCREMENT = 0;


CREATE TABLE device (
MAC_address VARCHAR(17) NOT NULL ,
device_password VARCHAR(255),
device_type_ID INT NOT NULL,
user_ID_device INT NOT NULL,
last_updated TIMESTAMP DEFAULT now(),
PRIMARY KEY (MAC_address),
FOREIGN KEY (device_type_ID) REFERENCES device_type(ID), 
FOREIGN KEY (user_ID_device) REFERENCES user(ID)
) AUTO_INCREMENT = 0;


CREATE TABLE data_type (
ID INT NOT NULL AUTO_INCREMENT,
data_category VARCHAR(255),
PRIMARY KEY (ID)
) AUTO_INCREMENT = 0;


CREATE TABLE input_data (
user_ID_data INT NOT NULL,
device_ID VARCHAR(17) NOT NULL,
data_type_ID INT NOT NULL,
input VARCHAR(255),
entry_time TIMESTAMP DEFAULT now(),
FOREIGN KEY (user_ID_data) REFERENCES user(ID),
FOREIGN KEY (device_ID) REFERENCES device(MAC_address),
FOREIGN KEY (data_type_ID) REFERENCES data_type(ID)
);