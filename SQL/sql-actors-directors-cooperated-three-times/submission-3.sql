-- Write your query below
with my_cte AS(SELECT actor_id, director_id, COUNT(*) AS count
FROM actor_director
GROUP BY actor_id, director_id)

SELECT actor_id, director_id
FROM my_cte
WHERE count >= 3;