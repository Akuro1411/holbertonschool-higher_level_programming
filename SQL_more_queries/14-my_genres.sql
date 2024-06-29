-- Finds the names of genres which Dexter contains
SELECT gen.name FROM tv_genres gen JOIN tv_show_genres sh ON sh.genre_id = gen.id WHERE sh.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');
