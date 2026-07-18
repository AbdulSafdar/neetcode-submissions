-- Write your query below
SELECT COALESCE(s.employee_id, e.employee_id) AS employee_id
FROM salaries AS s
FULL OUTER JOIN employees AS e
ON s.employee_id = e.employee_id
WHERE e.name IS NULL OR s.salary IS NULL;