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
        return self.__cursor.lastrowid  # Возвращаем ID новой записи

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

    def get_by_id(self, task_id: int) -> list:
        """Select task by id.

        Input:
            id (int)

        Output:
            task (list) :
                id (int)
                name (str)
                details (str)
        """
        __command = """
        SELECT id, name, details
        FROM tasks
        WHERE id = ?
        """
        self.__cursor.execute(__command, (task_id,))
        return self.__cursor.fetchone()

    def close(self, *, delete=False):
        """Clear database"""
        __command = "DROP TABLE IF EXISTS tasks"
        if delete:
            self.__cursor.execute(__command)
        self.__con.commit()
        self.__con.close()
