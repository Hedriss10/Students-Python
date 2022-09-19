from conection import Connnect
import psycopg2



con  = Connnect('pq://postgres:postgres123@localhost/aula_02')
sql = 'insert into cidade values (default , "Bahia"  ,  "BA")'

if con.manipulate(sql):
    print("Inserido com sucesso!")
print(con.fristPk("cidade", "id"))
rs =  con.consult("Select * from cidade")
for linha in rs:
    print(linha)
con.close()