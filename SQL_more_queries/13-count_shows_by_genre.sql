-- Counts the number of films in each genre and group them by their names
SELECT gen.name genre, COUNT(sh.genre_id) number_of_shows FROM tv_genres gen JOIN tv_show_genres sh ON gen.id = sh.genre_id GROUP BY gen.name ORDER BY COUNT(sh.genre_id) DESC;
