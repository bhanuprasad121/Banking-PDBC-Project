import mysql.connector
def mysql_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="bank_system"
    )
    return conn

