-- Write your query below
SELECT DISTINCT(c.title)
FROM tv_program AS t
LEFT JOIN content AS c
ON t.content_id = c.content_id
WHERE kids_content = 'Y' 
AND content_type = 'Movies'
AND (program_date LIKE '2020-06%')