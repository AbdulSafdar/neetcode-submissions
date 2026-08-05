-- Write your query below
with my_cte AS(
    SELECT *,
    RANK() OVER(PARTITION BY student_id ORDER BY SCORE DESC) AS rank
    FROM exam_results
),

my_cte2 AS(
    SELECT student_id, exam_id, score, RANK() OVER(PARTITION BY student_id ORDER BY exam_id ASC) AS rank2
FROM my_cte
WHERE rank = 1
ORDER BY student_id)

SELECT student_id, exam_id, score
FROM my_cte2
WHERE rank2 = 1