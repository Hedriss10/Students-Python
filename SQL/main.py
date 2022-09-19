import psycopg2

con = psycopg2.connect(host="localhost", database="aula_02",
                       user="hedris", password="Binfae@45")

cur = con.cursor()

# sql =  "create table cidade(id serial primary key, nome varchar(30), uf varchar(2))"
# cur.execute(sql)
# con.commit()

# sql =  "insert into cidade values (default, 'São Paulo', 'SP')"
# cur.execute(sql)
# con.commit()

cur.execute("select * from cidade")
result = cur.fetchall()
for rec in result:
    print(rec)
con.close()