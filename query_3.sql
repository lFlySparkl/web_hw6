SELECT g.id as group_id, g.group_name, AVG(e.grade) as avg_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN estimates e ON s.id = e.student_id
GROUP BY g.id, g.group_name
ORDER BY avg_grade DESC;