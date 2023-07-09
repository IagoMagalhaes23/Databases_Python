# Estudo sobre banco de dados com Python

## Resumo
Repositório para estudo de SQL e conexão com a linguagem Python.

## SQL Lite
Realizando a crianção de uma database com SQLite e algumas operações como leitura, escrita e busca utilizando a linguagem Python.
- Criando base de dados
connection = sqlite3.connect("alunos.db")

- Criando comunicação com base dados
cursor = connection.cursor()

- Base de dados
dados = [
    (2020, "Escola 1", "Reriutaba"),
    (2021, "Escola 2", "Sobral"),
    (2022, "Escola 3", "Fortaleza"),
    (2019, "Escola 4", "Varjota"),
    (2018, "Escola 5", "Cariré"),
]

- Criando tabela escolas
cursor.execute("create table escolas (ano integer, escola text, cidade text)")

- Preenchendo a tabela escolas
cursor.executemany("insert into escolas values (?,?,?)", dados)

- Exibindo todos os valores da tabela escola
print("******************************")
print("Tabela escolas")
for row in cursor.execute("select * from escolas"):
    print(row)
print("******************************")

- Exibindo as cidades da tabela escolas
print("******************************")
print("Cidades das escolas")
cursor.execute("select cidade from escolas")
cidades = cursor.fetchall()
print(cidades)
print("******************************")

- Exibindo o número de escolas
print("******************************")
print("Número de escolas")
cursor.execute("select cidade from escolas")
qtd_cidades = cursor.fetchall()
print(len(qtd_cidades))
print("******************************")

### Resultados
- Todos os valores da tabela escola <br>
![image](https://user-images.githubusercontent.com/65053026/224455058-41ff9d75-ae52-4395-a43f-8ef277380694.png) <br>

- Exibindo a coluna de cidades da tabela escola <br>
![image](https://user-images.githubusercontent.com/65053026/224455093-93cefb91-0ff1-4522-9f31-dd9e43d162b8.png) <br>

- Exibindo a quantidade de cidades da tabela escola <br>
![image](https://user-images.githubusercontent.com/65053026/224455111-ecdc6378-e816-431e-9364-71d42a358e22.png) <br>

## MySQL

## MongoDB

## PostgreSQl

