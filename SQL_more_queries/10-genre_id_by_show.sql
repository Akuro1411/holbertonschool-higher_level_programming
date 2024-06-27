-- Joins two table and shows title from one and genre from another one
SELECT sh.title, gen.genre_id FROM tv_shows sh NATURAL JOIN tv_show_genres gen ORDER BY sh.title ASC, gen.genre_id ASC;
