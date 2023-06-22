--part #1
SELECT title, release_year, category_id
From file INNER JOIN film_category on film_category.film_id = film.film_id;

--part #2
SELECT title, release_year, name
From film INNER JOIN film_category ON film_category.film_id=film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
WHERE name IN ('Action','Comedy','Family');

--part #3
SELECT ca.name category ,count(*) From file c
INNER JOIN film_category fc ON fc.film_id= c.film_id
INNER JOIN category ca ON ca.category_id =fc.category_id
group by 1;