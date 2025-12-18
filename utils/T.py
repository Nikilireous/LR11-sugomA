class Database_tasks:

    def __init__(self):
        import sqlite3
        self.__con = sqlite3.connect('mydata.db')
        self.__createtable()
        self.__cursor = self.__con.cursor()

    def __createtable(self):
        """Create database."""
        __command = """
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        details TEXT NOT NULL
        )"""
        self.__con.execute(__command)

    def add(self, task: list):
        """Add user to database.

        Input:
            task (list) :
                name (str)
                details (str)
        """
        __command = "INSERT INTO tasks (name, details) VALUES (?, ?)"
        self.__cursor.execute(__command, task)
        self.__con.commit()

    def update(self, task: list):
        """Update task details info by name.

        Input:
            task (list) :
                name (str)
                details (str)
        """
        __command = """
        UPDATE tasks
        SET details
        WHERE name = ?
        """
        self.__cursor.execute(__command, task[::-1])
        self.__con.commit()

    def delete(self, name: list):
        """Delete task from database by name.

        Input:
            name (str)
        """
        __command = """
        DELETE FROM tasks
        WHERE name = ?
        """
        self.__cursor.execute(__command, (name,))
        self.__con.commit()

    def select(self, name: str) -> list:
        """Select task by name.

        Input:
            name (str)

        Output:
            task (list) :
                name (str)
                details (str)
        """
        __command = """
        SELECT name, details
        FROM tasks
        WHERE name = ?
        """
        self.__cursor.execute(__command, (name,))
        return self.__cursor.fetchall()

    def close(self, *, delete='False'):
        """Clear database"""
        __command = "DROP TABLE IF EXISTS tasks"
        if delete:
            self.__cursor.execute(__command)
        self.__con.commit()
        self.__con.close()
