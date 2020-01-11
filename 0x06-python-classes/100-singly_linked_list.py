#!/usr/bin/python3
"""this module define a Node Class and a SinglyLinkedList"""


class Node():
    """Node class
    Attributes:
        attr1 (data): the data contained by the node
        attr2 (next_node): the next node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Node class
        Args:
            arg1 (self): the data contained by the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Args:
            arg1 (self): itself
            arg2 (value): the data contained by the node
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node
        Args:
            arg1 (self): itself
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node
        Args:
            arg1 (self): itself
            arg2 (value): the data contained by the node
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes at None"""
        self.__head = None

    def __str__(self):
        """prints the list"""
        final_string = ""
        top = self.__head
        while top is not None:
            final_string += "{}".format(top.data)
            top = top.next_node
            if top is not None:
                final_string += "\n"
        return final_string

    def sorted_insert(self, value):
        """Insert a new node"""
        top = self.__head
        node_new = Node(value, None)
        if top is None:
            self.__head = node_new
        else:
            pos = 0
            while top is not None:
                if top.data > value:
                    node_new.next_node = top
                    if pos == 0:
                        self.__head = node_new
                    break
                elif top.next_node is not None and top.next_node.data > value:
                        node_new.next_node = top.next_node
                        top.next_node = node_new
                        break
                elif top.next_node is None:
                    top.next_node = node_new
                    break
                top = top.next_node
                pos += 1
