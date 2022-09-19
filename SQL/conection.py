import psycopg2 

"""
    modularizando classe com conexão ,
    trabalhando com postgresql em OO
"""


class Connnect(object):
    _db = None
    
    def __init__(self, mhost, db, usr, pwd):
        self._db = psycopg2.connect(host=mhost, database=db,
                                    user=usr, password=pwd)
    def manipulate(self, sql):
        try:
                cur = self._db.cursor()
                cur.execute(sql)
                cur.close()
                self._db.commit()
        except:
            return False
        return True
    def consult(self, sql):
        rs = None
        try:
            cur =  self._db.cursor()
            cur.execute(sql)
            rs= cur.fetchall()
        except:
            return None
        return rs 
    
    def fristPk(self, table, key):
        sql = f'select max ("{key}") from ' + table 
        rs =  self.consult(sql)
        pk =  rs[0][0]
        return pk + 1
    
    def close(self):
        self._db.close()