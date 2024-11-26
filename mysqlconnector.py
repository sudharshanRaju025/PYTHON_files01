import mysql.connector
from mysql.connector import ProgrammingError

try:
    sql=mysql.connector.connect(host="localhost", user="root",password="raju_25**9876", database="mysql")

    print("connection tested")
except ProgrammingError as e:
    print(e)