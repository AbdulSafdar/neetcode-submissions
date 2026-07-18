-- Write your query below
SELECT MIN(p1.x - p2.x) AS shortest
FROM point AS p1
CROSS JOIN point AS p2
WHERE p1.x > p2.x