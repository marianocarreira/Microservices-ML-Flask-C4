from datetime import datetime

class LogEntry:
    def __init__(self, _id, _datetime, _data, _type):
        self._id = _id
        self._datetime = _datetime
        self._data = _data
        self._type = _type

    @property
    def id(self):
        return self._id

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

def theMethod():
    print("jello")