class Database_users:

    def __init__(self):
        import sqlite3
        self.__con = sqlite3.connect('mydata.db')
        self.__createtable()
        self.__cursor = self.__con.cursor()

    def __createtable(self):
        """Create database."""
        __command = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        );"""
        self.__con.execute(__command)

    def add(self, user: list):
        """Add user to database.

        Input:
            user (list) :
                name (str)
                email (str)
                password (str)
        """
        __command = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
        self.__cursor.execute(__command, user)
        self.__con.commit()

    def update(self, user: list):
        """Update user info by email.

        Input:
            user (list) :
                name (str)
                email (str)
                password (str)
        """
        __command = """
        UPDATE users
        SET name = ?, password = ?
        WHERE email = ?
        """
        self.__cursor.execute(__command, (user[0], user[2], user[1]))
        self.__con.commit()

    def delete(self, email: list):
        """Delete user from database by email.

        Input:
            email (str)
        """
        __command = """
        DELETE FROM users
        WHERE email = ?
        """
        self.__cursor.execute(__command, (email,))
        self.__con.commit()

    def select(self, email: str) -> list:
        """Select user by email.

        Input:
            email (str)

        Output:
            user (list) :
                name (str)
                id (int)
                email (str)
                password (str)
        """
        __command = """
        SELECT name, id, email, password
        FROM users
        WHERE email = ?
        """
        self.__cursor.execute(__command, (email,))
        return self.__cursor.fetchall()

    def close(self, *, delete='False'):
        """Clear database"""
        __command = "DROP TABLE IF EXISTS users"
        if delete:
            self.__cursor.execute(__command)
        self.__con.commit()
        self.__con.close()
