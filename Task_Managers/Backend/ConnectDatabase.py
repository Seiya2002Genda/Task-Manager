import mysql.connector
from Task_Managers.Backend.Config import Config

class ConnectDatabase:

    def connect(self):
        return mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE
        )