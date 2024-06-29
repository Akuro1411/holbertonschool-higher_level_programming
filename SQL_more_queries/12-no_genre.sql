-- Joins two table and shows title from one and genre from another one.NULL values also are included
SELECT sh.title, gen.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres gen ON sh.id = gen.show_id WHERE gen.genre_id is NULL ORDER BY sh.title ASC, gen.genre_id ASC;
