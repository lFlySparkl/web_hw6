SELECT t.id as teacher_id, t.teacher_name, AVG(e.grade) as avg_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
JOIN estimates e ON s.id = e.subject_id
GROUP BY t.id, t.teacher_name;