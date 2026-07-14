-- Write your query below
SELECT name AS warehouse_name, SUM(p.width * p.length * p.height * w.units) AS volume
FROM warehouse AS w
LEFT JOIN products AS p
ON w.product_id = p.product_id
GROUP BY name