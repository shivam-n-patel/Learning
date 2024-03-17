import mysql.connector

class DatabaseManager:
    
    def __init__(self, user, password, host) -> None:
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )

        self.cursor =  self.connection.cursor()

    def create_database(self, db_name):
        print(self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

    def delete_database(self, db_name):
        print(self.cursor.execute(f"DROP DATABASE IF EXISTS {db_name}"))
        

    def fect_databases(self):
        self.cursor.execute("SHOW DATABASES")
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


def main():
    
    database_connection = DatabaseManager(
        user = 'root',
        password = '12345678',
        host = 'localhost'
    )

    try:
        database_connection.create_database("djangoCRM")
        

    finally:
        database_connection.close_connection()
        print("-------------------------PROGRAM TERMINATION-------------------------")

if __name__ == "__main__":
    main()
