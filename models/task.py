class Task:

    def __init__(self, name, id, details):
        self.__name = name
        self.__id = id
        self.__details = details

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
    def details(self):
        return self.__details

    @details.setter
    def details(self, details: str):
        if type(details) is str and len(details) > 0:
            self.__details = details
        else:
            raise ValueError("Параметр details задан некорректно")

