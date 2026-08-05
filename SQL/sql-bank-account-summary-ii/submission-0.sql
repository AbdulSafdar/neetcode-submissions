-- Write your query below
SELECT name, SUM(amount) AS balance
FROM users AS u
LEFT JOIN transactions AS t
ON u.account = t.account
GROUP BY name
HAVING SUM(amount) > 10000