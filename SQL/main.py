<<<<<<< HEAD
"""
    Autor: Iago Magalhães
    Descrição: Comandos básicos de SQL utilizando Python e SQLite
"""

import sqlite3

#Criando base de dados
connection = sqlite3.connect("alunos.db")

#Criando comunicação com base dados
cursor = connection.cursor()

#Base de dados
dados = [
    (2020, "Escola 1", "Reriutaba"),
    (2021, "Escola 2", "Sobral"),
    (2022, "Escola 3", "Fortaleza"),
    (2019, "Escola 4", "Varjota"),
    (2018, "Escola 5", "Cariré"),
]

#Criando tabela escolas
cursor.execute("create table escolas (ano integer, escola text, cidade text)")

#Preenchendo a tabela escolas
cursor.executemany("insert into escolas values (?,?,?)", dados)

#Salvando alterações
connection.commit()

#Exibindo todos os valores da tabela escola
print("******************************")
print("Tabela escolas")
for row in cursor.execute("select * from escolas"):
    print(row)
print("******************************")

#Exibindo as cidades da tabela escolas
print("******************************")
print("Cidades das escolas")
cursor.execute("select cidade from escolas")
cidades = cursor.fetchall()
print(cidades)
print("******************************")

#Exibindo o número de escolas
print("******************************")
print("Número de escolas")
cursor.execute("select cidade from escolas")
qtd_cidades = cursor.fetchall()
print(len(qtd_cidades))
print("******************************")

#Fechando conexão com base de dados
=======
"""
    Autor: Iago Magalhães
    Descrição: Comandos básicos de SQL utilizando Python e SQLite
"""

import sqlite3

#Criando base de dados
connection = sqlite3.connect("alunos.db")

#Criando comunicação com base dados
cursor = connection.cursor()

#Base de dados
dados = [
    (2020, "Escola 1", "Reriutaba"),
    (2021, "Escola 2", "Sobral"),
    (2022, "Escola 3", "Fortaleza"),
    (2019, "Escola 4", "Varjota"),
    (2018, "Escola 5", "Cariré"),
]

#Criando tabela escolas
cursor.execute("create table escolas (ano integer, escola text, cidade text)")

#Preenchendo a tabela escolas
cursor.executemany("insert into escolas values (?,?,?)", dados)

#Salvando alterações
connection.commit()

#Exibindo todos os valores da tabela escola
print("******************************")
print("Tabela escolas")
for row in cursor.execute("select * from escolas"):
    print(row)
print("******************************")

#Exibindo as cidades da tabela escolas
print("******************************")
print("Cidades das escolas")
cursor.execute("select cidade from escolas")
cidades = cursor.fetchall()
print(cidades)
print("******************************")

#Exibindo o número de escolas
print("******************************")
print("Número de escolas")
cursor.execute("select cidade from escolas")
qtd_cidades = cursor.fetchall()
print(len(qtd_cidades))
print("******************************")

#Fechando conexão com base de dados
>>>>>>> 4564f8b69bb7de82137175fe8f053556391578cb
connection.close()