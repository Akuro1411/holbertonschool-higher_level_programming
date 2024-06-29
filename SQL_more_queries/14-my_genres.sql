-- Finds the names of genres which Dexter contains
SELECT gen.name FROM tv_genres gen JOIN tv_show_genres sh ON sh.genre_id = gen.id JOIN tv_shows tv WHERE tv.title = 'Dexter' AND tv.id = sh.show_id ORDER BY gen.name ASC;
