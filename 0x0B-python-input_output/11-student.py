#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary of Student with conditions to filter
        """

        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            dict = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    dict[i] = self.__dict__[i]
            return dict

    def reload_from_json(self, json):
        """eplaces all attributes of the Student instance"""

        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
            if key == "age":
                self.age = value
