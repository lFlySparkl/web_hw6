SELECT s.student_name, e.grade
FROM students s
JOIN estimates e ON s.id = e.student_id
WHERE s.group_id = :group_id AND e.subject_id = :subject_id;