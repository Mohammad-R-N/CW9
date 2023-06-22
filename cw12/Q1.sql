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

--part #4
SELECT name,count(*) as count
From film INNER JOIN film_category ON film_category.film_id = film.film_id
INNER JOIN category ON category.category_id=film_category.category_id
group by name
HAVING count(*) >60 AND count(*)<68;

--part #5
SELECT language.name language,film.title,category.name category
From film INNER JOIN language ON language.language_id=film.language_id
INNER  JOIN film_category ON film_category.film_id = film.film_id;

--part #6
SELECT customer.film_name,customer.last_name, file.title,AGE(return_date,rental_date) as rental_duration
From customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN inventory ON inventory.inventory_id=rental.inventory_id
INNER JOIN film ON film.film_id= inventory.inventory_id;

--part #7
select * from film
where film.length > (select avg(length) from film);
