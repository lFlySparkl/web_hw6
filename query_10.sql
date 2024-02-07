SELECT sub.subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON s.group_id = group_id
WHERE s.id = :student_id AND t.id = :teacher_id;