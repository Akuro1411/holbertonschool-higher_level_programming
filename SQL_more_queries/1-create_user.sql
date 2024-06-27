-- Creates a user on localhost and give all privilages to it
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd';
GRANT ALL PRIVILAGES ON *.* to 'user_0d_1'@'localhost';
