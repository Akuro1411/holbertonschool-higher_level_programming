-- Creates table with value which can't be NULL
CREATE TABLE IF NOT EXISTS force_name
(
	id INT,
	name VARCHAR(256) NOT NULL
)
