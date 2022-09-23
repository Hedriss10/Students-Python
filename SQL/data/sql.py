import sqlite3 as sql 


conection  = sql.connect('basededados.db')
cursor =  conection.cursor()

"""
    migrando a tabela de dados com sqlite3,
    criando a tabela clientes,
"""

# cursor.execute(
#     'CREATE TABLE cliente("nome" varchar(30) , "idade" INTEGER)'
# )

# cursor.execute(
#     'INSERT INTO cliente (nome, idade) VALUES ("Henrique" , 20)'
# )

consult = cursor.execute("SELECT * FROM cliente")

for x in consult:
    print(x)


conection.commit()
