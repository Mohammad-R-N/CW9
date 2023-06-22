--part #1
SELECT title, release_year, category_id
From file INNER JOIN film_category on film_category.film_id = film.film_id;