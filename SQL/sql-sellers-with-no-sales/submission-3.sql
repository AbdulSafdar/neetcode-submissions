-- Write your query below
WITH my_cte AS (
    SELECT
        s.seller_id,
        s.seller_name,
        o.sale_date,
        EXTRACT(YEAR FROM o.sale_date) AS year
    FROM seller AS s
    LEFT JOIN orders AS o
        ON s.seller_id = o.seller_id
)

SELECT DISTINCT(seller_name)
FROM my_cte
WHERE seller_id  NOT IN (SELECT seller_id
FROM my_cte
WHERE year = 2020
)
ORDER BY seller_name ASC
;

