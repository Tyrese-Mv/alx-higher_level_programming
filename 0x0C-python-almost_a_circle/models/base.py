#!/usr/bin/python3

"""Base Module"""
import json

class Base:
    """Base Class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(list_objs[0].__class__.__name__), "w") as file:
            if list_objs is None:
                objects = []
            else:
                objects = [x.to_dictionary() for x in list_objs]
            file.write(cls.to_json_string(objects))
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if "size" in dictionary.keys():
            obj =  Square(1)
        elif "width" in dictionary.keys():
            obj =  Rectangle(1, 1)
        else:
            return None
        obj.update(**dictionary)
        return obj
