-- Finds the total number of each score. Group by was used on this task
SELECT score, COUNT(score) "number" FROM second_table GROUP BY score ORDER BY "number" DESC;
