-- Shows the film titles with their genres
SELECT sh.title, tv.name FROM tv_shows sh LEFT JOIN tv_show_genres gen ON gen.show_id = sh.id LEFT JOIN tv_genres tv ON tv.id = gen.genre_id ORDER BY sh.title ASC, tv.name ASC;
