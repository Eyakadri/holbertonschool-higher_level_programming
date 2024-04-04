#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {
                key: getattr(self, key)
                for key in sorted(self.__dict__.keys())
            }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
