-- Finds the films at the Comedy genre
SELECT tv.title FROM tv_shows tv JOIN tv_show_genres gen ON gen.show_id = tv.id JOIN tv_genres sh ON sh.id = gen.genre_id WHERE sh.name = 'Comedy' ORDER BY tv.title;
