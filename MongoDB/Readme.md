## Introdução
Neste repositório é apresentado uma pequena aplicação de exemplo de como utilizar o MongoDB junto ao Python, através da lib PyMongo algumas funcionalidades são apresentadas e executadas.

## Comandos
- Criando coleção no MongoDB

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

- Inserindo dados no MongoDB

    x = mycol.insert_one(mydict)

- Busca de dados no MongoDB

    x = mycol.find_one()

- Ordenação de dados no MongoDB

    mydoc = mycol.find().sort("name")

- Excluir dados no MongoDB

    myquery = { "address": "Mountain 21" }
    mycol.delete_one(myquery)

- Atualização de dados no MongoDB

    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }

    mycol.update_one(myquery, newvalues)

## Referências
- https://www.w3schools.com/python/python_mongodb_getstarted.asp