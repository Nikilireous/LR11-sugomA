from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, name, id, email, password):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) is str and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Параметр name задан некорректно")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if type(id) is int and id >= 0:
            self.__id = id
        else:
            raise ValueError("Параметр id задан некорректно")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if type(email) is str and len(email) > 0 and "@" in email:
            self.__email = email
        else:
            raise ValueError("Параметр email задан некорректно")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        if type(password) is str and len(password) >= 0:
            self.__password = password
        else:
            raise ValueError("Параметр password задан некорректно")

