#!/usr/bin/python3
"""module for a singly linked list"""


class Node:
    """"this class defines a node"""

    def __init__(self, data, next_node=None):
        """
        Args:
            data:the data of the node
            next_node: the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data """

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute"""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set  next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """this class defines a singly linked list"""

    def __init__(self):
                """
        Args:
            head:the head of the list
        """

        self.head = None

    def __str__(self):
        """make list printable"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new