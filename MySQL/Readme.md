## Introdução
Neste repositório é apresentado uma pequena aplicação de exemplo de como utilizar o MySQL junto ao Python, através da lib mysql algumas funcionalidades são apresentadas e executadas.

## Comandos
- Configurações iniciais

    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )

    mycursor = mydb.cursor()

- Criando um database no MySQL

    mycursor.execute("CREATE DATABASE mydatabase")

- Criando tabela no MySQL

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

- Inserindo dados em uma tabela MySQL

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

- Seleção no MySQL

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

- Busca de dados no MySQL

    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

- Ordenando dados no MySQL

    sql = "SELECT * FROM customers ORDER BY name"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

- Excluindo dados no MySQL

    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

    mycursor.execute(sql)

    mydb.commit()

-  Atualizando dados no MySQL

    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

    mycursor.execute(sql)

    mydb.commit()

## Referências
- https://www.w3schools.com/python/python_mysql_getstarted.asp