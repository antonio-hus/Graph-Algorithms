# This module contains the representation of the class Vertex

# VERTEX REPRESENTATION BELOW
class Vertex:

    # CLASS INITIALIZATION
    def __init__(self, number: int):
        """
        Initializes a Vertex Object having a unique ID
        :param number: The ID (Integer Number) of the Vertex
        """
        self.__number = number

    # CLASS PROPERTIES
    @property
    def number(self):
        """
        :return: The Vertex ID ( Number )
        """
        return self.__number

    # FORMATTING OPTIONS
    def __str__(self):
        """
        String Representation of a Vertex
        """
        return f"Vertex | NumID: {self.number}"

    def __eq__(self, other):
        """
        Equality condition of vertices ( Tests for equal IDs )
        """
        return self.number == other.number

    def __hash__(self):
        """
        :return: Hashed form of a Vertex ( Represented by the ID )
        """
        return hash(self.number)
