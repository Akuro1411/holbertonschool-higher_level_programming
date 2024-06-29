-- Joins two table and shows title from one and genre from another one
SELECT sh.title, gen.genre_id FROM tv_shows sh JOIN tv_show_genres gen ON sh.id = gen.show_id ORDER BY sh.title ASC, gen.genre_id ASC;
