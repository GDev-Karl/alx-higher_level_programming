#!/usr/bin/python3
""" Base Module """
import json
import csv
import turtle


class Base:
    """
    Represent the base for the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionnaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write a JSon serialization if the list of object is a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialization of a JSON string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class instantied from a dictionary of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        classes instantiated from a file of JSON strings.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        CSV serialization of a list of objects to a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        list of classes instantiated from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Rectangles and Squares using the turtle moDULE
        """
        turtObject = turtle.Turtle()
        turtObject.screen.bgcolor("#b7312c")
        turtObject.pensize(3)
        turtObject.shape("turtle")

        turtObject.color("#ffffff")
        for rect in list_rectangles:
            turtObject.showturtle()
            turtObject.up()
            turtObject.goto(rect.x, rect.y)
            turtObject.down()
            for i in range(2):
                turtObject.forward(rect.width)
                turtObject.left(90)
                turtObject.forward(rect.height)
                turtObject.left(90)
            turtObject.hideturtle()

        turtObject.color("#b5e3d8")
        for square in list_squares:
            turtObject.showturtle()
            turtObject.up()
            turtObject.goto(square.x, square.y)
            turtObject.down()
            for i in range(2):
                turtObject.forward(square.width)
                turtObject.left(90)
                turtObject.forward(square.height)
                turtObject.left(90)
            turtObject.hideturtle()

        turtle.exitonclick()
