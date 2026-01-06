class Database_user_task:

    def __init__(self):
        import sqlite3
        self.__con = sqlite3.connect('mydata.db')
        self.__createtable()
        self.__cursor = self.__con.cursor()

    def __createtable(self):
        """Create database."""
        __command = """
        CREATE TABLE IF NOT EXISTS user_task(
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        priority INTEGER NOT NULL,
        status TEXT NOT NULL,
        date TEXT NOT NULL,
        user_id  INTEGER NOT NULL,
        task_id INTEGER NOT NULL
        )"""
        self.__con.execute(__command)

    def add(self, task: list):
        """Add task to database.

        Input:
            task (list) :
                priority (int)
                status (str)
                date (str)
                user_id (int)
                task_id (int)
        """
        __command = "INSERT INTO user_task (priority, status, date, user_id, task_id) VALUES (?, ?, ?, ?, ?)"
        self.__cursor.execute(__command, task)
        self.__con.commit()
        return self.__cursor.lastrowid

    def update(self, task: list):
        """Update task in database by task_id and user_id.

        Input:
            task (list) :
                priority (int)
                status (str)
                date (str)
                user_id (int)
                task_id (int)
        """
        __command = """
        UPDATE user_task
        SET priority = ?, status = ?, date = ?
        WHERE user_id = ? AND task_id = ?
        """
        self.__cursor.execute(__command, task)
        self.__con.commit()

    def delete(self, task: list):
        """Delete task from database by user_id and task_id.

        Input:
            task (list) :
                priority (int)
                status (str)
                date (str)
                user_id (int)
                task_id (int)
        """
        __command = """
        DELETE FROM user_task
        WHERE user_id = ? AND task_id = ?
        """
        self.__cursor.execute(__command, task[3:5])
        self.__con.commit()

    def select(self, user_id: int) -> list[list]:
        """Select tasks of user by user_id.

        Input:
            user_id (int)

        Output:
            task_list (list) :
                task (list) :
                    priority (int)
                    status (str)
                    date (str)
                    user_id (int)
                    task_id (int)
        """
        __command = """
        SELECT priority, status, date, user_id, task_id
        FROM user_task
        WHERE user_id = ?
        """
        self.__cursor.execute(__command, (user_id,))
        return self.__cursor.fetchall()


    def close(self, *, delete=False):
        """Clear database"""
        __command = "DROP TABLE IF EXISTS user_task"
        if delete:
            self.__cursor.execute(__command)
        self.__con.commit()
        self.__con.close()
