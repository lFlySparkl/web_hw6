SELECT e.grade, e.time_rating
FROM estimates e
JOIN subjects sub ON e.subject_id = sub.id
JOIN students s ON e.student_id = s.id
JOIN groups g ON s.group_id = g.id
WHERE g.id = :group_id AND sub.id = :subject_id
ORDER BY e.time_rating;