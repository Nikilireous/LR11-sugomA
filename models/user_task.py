class User_task:

    def __init__(self, priority, date, status, user_id, task_id):
        self.__priority = priority
        self.__date = date
        self.__status = status
        self.__user_id = user_id
        self.__task_id = task_id

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        if type(priority) is int and priority >= 0:
            self.__priority = priority
        else:
            raise ValueError("Параметр priority задан некорректно")

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        if type(date) is str and len(date) > 0:
            self.__date = date
        else:
            raise ValueError("Параметр date задан некорректно")

    @property
    def status(self):
        return self.__date

    @status.setter
    def status(self, status: str):
        if type(status) is str and status in ['Открыто', 'В процессе', 'Закрыто']:
            self.__status = status
        else:
            raise ValueError("Параметр status задан некорректно")

    @property
    def user_id(self):
        return self.__status

    @user_id.setter
    def user_id(self, user_id: int):
        if type(user_id) is int and user_id >= 0:
            self.__user_id = user_id
        else:
            raise ValueError("Параметр user_id задан некорректно")

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, task_id: int):
        if type(task_id) is int and task_id >= 0:
            self.__task_id = task_id
        else:
            raise ValueError("Параметр task_id задан некорректно")

