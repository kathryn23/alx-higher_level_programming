#!/usr/bin/python3
"""
Task 2: Write the class Rectangle that inherits from Base
Task 3: Update the class Rectangle by adding validation of all setter
        methods and instantiation (id excluded)
Task 4: Update the class Rectangle by adding the public method def area
        (self): that returns the area value of the Rectangle instance.
Task 5: Update the class Rectangle by adding the public method def display
        (self): that prints in stdout the Rectangle instance with the
        character #
Task 6: Update the class Rectangle by overriding the __str__ method so that
        it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
Task 7: Update the class Rectangle by improving the public method def
        display(self): to print in stdout the Rectangle instance with the
        character # by taking care of x and y
Task 8: Update the class Rectangle by adding the public method def update
        (self, *args): that assigns an argument to each attribute
Task 9: Update the class Rectangle by updating the public method def update
        (self, *args): by changing the prototype to update(self, *args,
        **kwargs) that assigns a key/value argument to attributes
Task 13:Update the class Rectangle by adding the public method def
        to_dictionary(self): that returns the dictionary representation of
        a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base

    Why private attributes with getter/setter? Why not directly
    public attribute?

    Because we want to protect attributes of our class.
    With a setter, you are able to validate what a developer
    is trying to assign to a variable. So after, in your class
    you can “trust” these attributes.

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
            width ([type]): [private instance attribute]
            height ([type]): [private instance attribute]
            x (int, optional): [private instance attribute]. Defaults to 0.
            y (int, optional): [private instance attribute]. Defaults to 0.

            id ([type], optional): [ super class with id]. Defaults to None.
            this super call use the logic of the __init__ of the Base class

            use of super():
            https://www.programiz.com/python-programming/methods/built-in/super
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method area

        Returns:
            [int]: [returns the area value of the Rectangle instance]
        """
        return self.__width * self.__height

    def display(self):
        """Public method display the rectangle by taking care of x and y"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overriding the __str__ method so that it returns a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """update the attributes of the class with the key-worded
        and non-key-worded arguments]

        The setattr() function sets the value of the attribute of an object.
        setattr(object, name, value)

        for n in range(len(args)):
            if n is 0:
                self.id = args[0]
            elif n is 1:
                self.width = args[1]
            elif n is 2:
                self.height = args[2]
            elif n is 3:
                self.x = args[3]
            elif n is 4:
                self.y = args[4]
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args is None or not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            for n in range(len(args)):
                setattr(self, attr[n], args[n])

    def to_dictionary(self):
        """method that returns the dictionary representation
        of a Rectangle"""
        return dict(id=self.id, x=self.__x, y=self.__y,
                    width=self.__width, height=self.__height)
