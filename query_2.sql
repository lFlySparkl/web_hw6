-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.id, s.student_name, AVG(e.grade) as avg_grade
FROM students s
JOIN estimates e ON s.id = e.student_id
WHERE e.subject_id = (
    SELECT subject_id
    FROM estimates
    GROUP BY subject_id
    ORDER BY AVG(grade) DESC
    LIMIT 1
)
GROUP BY s.id, s.student_name
ORDER BY avg_grade DESC
LIMIT 1;

