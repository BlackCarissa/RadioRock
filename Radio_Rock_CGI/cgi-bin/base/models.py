from .base import DataBase
import re
from string import ascii_letters

class people(): # ВСЕ КАРТЫ. Идет наследование от Model 
#  ФИО клиента Номер паспорта Адрес Номер телефона
    def __init__(self,db,base_name,login,password,email):
        self.__db = db

        self._id=self.__db.save(base_name,(login,password,email))