SELECT s.student_name, sb.subject_name
FROM students s
JOIN estimates e ON s.id = e.student_id
JOIN subjects sb ON e.subject_id = sb.id;