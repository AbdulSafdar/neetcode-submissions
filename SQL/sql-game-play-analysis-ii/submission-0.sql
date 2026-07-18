-- Write your query below
SELECT a.player_id, device_id
FROM activity AS a
JOIN (SELECT player_id, 
MIN(event_date) AS first_login
FROM activity
GROUP BY player_id) AS a2
ON a.player_id = a2.player_id 
AND a2.first_login = a.event_date