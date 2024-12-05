import math
import copy

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}
        self.neighbors = {}

    