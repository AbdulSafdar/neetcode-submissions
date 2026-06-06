-- Write your query below
SELECT
ROUND(SUM(CASE WHEN 
customer_pref_delivery_date - order_date = 0 THEN 1 ELSE 0
END) * 100.0 / COUNT(delivery_id),2) AS immediate_percentage
FROM delivery
