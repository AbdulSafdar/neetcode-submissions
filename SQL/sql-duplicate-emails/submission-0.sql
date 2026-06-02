-- Write your query below
SELECT DISTINCT(email)
FROM person
GROUP BY email
HAVING COUNT(email) > 1