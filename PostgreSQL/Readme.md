## Introdução
Neste repositório é apresentado uma pequena aplicação de exemplo de como utilizar o PostgreSQL junto ao Python, através da lib psycopg2 algumas funcionalidades são apresentadas e executadas.

## Comandos
- Configuranções iniciais

    conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")

    cursor = conn.cursor()

- Lendo dados de uma tabela no PostgreSQL

    cursor.execute("SELECT * FROM DB_table WHERE id = 1")
    print(cursor.fetchone())

## Referências
- https://www.freecodecamp.org/news/postgresql-in-python/