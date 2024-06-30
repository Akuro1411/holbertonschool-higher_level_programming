-- Describes all the data from table
SELECT 'first_tableCREATETABLE`first_table`(
`id`intNOTNULLAUTO_INCREMENT,
`name`varchar(128)DEFAULTNULL,
`c`char(1)DEFAULTNULL,
`created_at`dateDEFAULTNULL,
PRIMARYKEY(`id`)
)ENGINE=InnoDBDEFAULTCHARSET=utf8mb4COLLATE=utf8mb4_0900_ai_ci' FROM dual;
