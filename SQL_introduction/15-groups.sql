-- lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS count FROM `second_table` GROUP BY score;