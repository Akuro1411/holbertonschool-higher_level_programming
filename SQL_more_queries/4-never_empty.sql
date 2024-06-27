-- Creates table with value which can't be NULL
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
