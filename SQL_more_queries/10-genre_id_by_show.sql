SELECT sh.title, gen.genre_id FROM tv_shows sh NATURAL JOIN tv_show_genres gen ORDER BY sh.title, gen.genre_id ASC;
