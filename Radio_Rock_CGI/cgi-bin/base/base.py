from genericpath import exists
import sqlite3
import os
import shutil



class DataBase:
    path = os.path.abspath("bd.db")

    def __init__(self, create_base = False):
        if not exists(self.path): # если базы нет -> создать файл
            create_base = True
        self.__db = sqlite3.connect(self.path) # подключаем базу
        self.__db.row_factory = sqlite3.Row
        self.__cur = self.__db.cursor() # подключаем курсор
        if create_base: # создаем базу методом сreate_db, если ее нет
            self.create_db('PEOPLE_LIST')
        #print('ПОДКЛЮЧИЛСИЬ К БАЗЕ')
    def __del__(self): 
        self.__db.close()

    def create_db(self,name_table): # создание базы
        with sqlite3.connect(self.path) as con:
            cur = con.cursor()
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {name_table} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT,
                    password TEXT,
                    email TEXT
                )""")

    def validate(self,login,password):
        try:
            self.__cur.execute(f"SELECT * FROM PEOPLE_LIST WHERE login = '{login}' AND password = '{password}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return True
            else: return False
        except sqlite3.Error as e:
            return False

    
# СОХРАНЕНИЕ 
    def save(self, table_name, params):# INSERT INTO orders VALUES(NULL, ?, ?, ?), (1,2,3)
        try:
            qr = "?," * len(params)
            print(f"INSERT INTO {table_name} VALUES(null,{qr[:-1]})", params)
            self.__cur.execute(f"INSERT OR IGNORE INTO {table_name} VALUES(null,{qr[:-1]})", params)
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления в БД "+str(e))
            return False
        return self.__cur.lastrowid
