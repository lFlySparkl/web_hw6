-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.id, s.student_name, AVG(e.grade) as avg_grade
FROM students s
JOIN estimates e ON s.id = e.student_id
GROUP BY s.id, s.student_name
ORDER BY avg_grade DESC
LIMIT 5;