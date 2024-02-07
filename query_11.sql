SELECT AVG(e.grade) as average_grade
FROM estimates e
JOIN subjects sub ON e.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON e.student_id = s.id
WHERE s.id = :student_id AND t.id = :teacher_id;