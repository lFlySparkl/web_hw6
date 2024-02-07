from sqlalchemy import create_engine, text

# Підключення до бази даних
engine = create_engine('postgresql://myuser:1111@localhost:5432/mydatabase')

# Створення текстового об'єкту SQL-запиту
# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql_query = text("""
    SELECT s.id, s.student_name, AVG(e.grade) as avg_grade
    FROM students s
    JOIN estimates e ON s.id = e.student_id
    GROUP BY s.id, s.student_name
    ORDER BY avg_grade DESC
    LIMIT 5;
""")

# 2. Знайти студента із найвищим середнім балом з певного предмета.
# sql_query = text("""
#     SELECT s.id, s.student_name, AVG(e.grade) as avg_grade
#     FROM students s
#     JOIN estimates e ON s.id = e.student_id
#     WHERE e.subject_id = (
#         SELECT subject_id
#         FROM estimates
#         GROUP BY subject_id
#         ORDER BY AVG(grade) DESC
#         LIMIT 1
# )
# GROUP BY s.id, s.student_name
# ORDER BY avg_grade DESC
# LIMIT 1;
# """)

# 3. Знайти середній бал у групах з певного предмета.
# sql_query = text("""
#     SELECT g.id as group_id, g.group_name, AVG(e.grade) as avg_grade
#     FROM groups g
#     JOIN students s ON g.id = s.group_id
#     JOIN estimates e ON s.id = e.student_id
#     GROUP BY g.id, g.group_name
#     ORDER BY avg_grade DESC;
# """)

# 4. Знайти середній бал на потоці (по всій таблиці оцінок).
# sql_query = text("""
#     SELECT AVG(grade) as avg_grade
#     FROM estimates;
# """)

# # 5. Знайти які курси читає певний викладач.
# sql_query = text("""
#     SELECT t.id as teacher_id, t.teacher_name, s.subject_name
#     FROM teachers t
#     JOIN subjects s ON t.id = s.teacher_id;
# """)

# # 6. Знайти список студентів у певній групі.
# group_id = 1  # Замініть на потрібне значення 1,2,3
# sql_query = text("""
#     SELECT s.id as student_id, s.student_name, g.group_name
#     FROM students s
#     JOIN groups g ON s.group_id = g.id
#     WHERE g.id = :group_id;
# """).bindparams(group_id=group_id)

# # 7 Знайти оцінки студентів у окремій групі з певного предмета.
# group_id = 1  # Замініть на потрібне значення 1,2,3
# subject_id = 2 # Замініть на потрібне значення 1,2,3,4,5
# sql_query = text("""
#     SELECT s.student_name, e.grade
#     FROM students s
#     JOIN estimates e ON s.id = e.student_id
#     WHERE s.group_id = :group_id AND e.subject_id = :subject_id;
# """).bindparams(group_id=group_id, subject_id=subject_id)

# # 8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
# sql_query = text("""
#     SELECT t.id as teacher_id, t.teacher_name, AVG(e.grade) as avg_grade
#     FROM teachers t
#     JOIN subjects s ON t.id = s.teacher_id
#     JOIN estimates e ON s.id = e.subject_id
#     GROUP BY t.id, t.teacher_name;
# """)

# # 9 Знайти список курсів, які відвідує студент.
# sql_query = text("""
#     SELECT s.student_name, sb.subject_name
#     FROM students s
#     JOIN estimates e ON s.id = e.student_id
#     JOIN subjects sb ON e.subject_id = sb.id;
# """)

# # 10 Список курсів, які певному студенту читає певний викладач.
# student_id = 1  # Замініть на потрібне значення 1-30
# teacher_id = 2 # Замініть на потрібне значення 1,2,3
# sql_query = text("""
#     SELECT sub.subject_name
#     FROM subjects sub
#     JOIN teachers t ON sub.teacher_id = t.id
#     JOIN students s ON s.group_id = group_id
#     WHERE s.id = :student_id AND t.id = :teacher_id;
# """).bindparams(student_id=student_id, teacher_id=teacher_id)

# Виконання SQL-запиту через cursor.execute
with engine.connect() as connection:
    result = connection.execute(sql_query)

    # Отримання результатів
    for row in result:
        print(row)

# with engine.connect() as connection:
#     result = connection.execute(sql_query, group_id=group_id)

#     # Отримання результатів
#     for row in result:
#         print(row)