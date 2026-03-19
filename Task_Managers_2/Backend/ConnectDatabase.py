import mysql.connector
from mysql.connector import Error
from Task_Managers_2.Backend.Config import Config


class ConnectDatabase:
    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DATABASE
            )
            return connection
        except Error as e:
            raise RuntimeError(f"Database connection failed: {e}")