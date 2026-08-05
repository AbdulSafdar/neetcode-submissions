-- Write your query below
WITH my_cte AS(SELECT team_id, COUNT(team_id) AS team_size
FROM employee
GROUP BY team_id)

SELECT employee_id, team_size
FROM my_cte AS c
LEFT JOIN employee AS e
ON c.team_id = e.team_id