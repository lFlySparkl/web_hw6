создаем контейнер
docker run --name my_postgres_container -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=1111 -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres

запускаем контейнер
docker start my_postgres_container

запускаем "main.py" для создания и наполнения таблиц

далее проверяем sql запросы вручную из файлов "query_number.sql" или из файла "cursor_execute_sql.py"