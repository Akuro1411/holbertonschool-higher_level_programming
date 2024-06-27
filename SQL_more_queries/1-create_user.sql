-- Creates a user on localhost and give all privilages to it
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILAGES ON *.* to 'user_0d_1';
