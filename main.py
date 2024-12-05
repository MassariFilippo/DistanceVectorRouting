import math
import copy

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        """Add a neighboring node with its direct distance"""
        self.neighbors[neighbor.name] = {
            'node': neighbor,
            'distance': distance
        }
        # Initialize routing table entry for this neighbor
        self.routing_table[neighbor.name] = distance

    def update_routing_table(self):
        """Perform Distance Vector Routing algorithm update"""
        updated = False
        for dest, current_dist in list(self.routing_table.items()):
            # Skip direct neighbors in initial routing
            if dest == self.name:
                continue

            # Check routes through each neighbor
            for neighbor_name, neighbor_info in self.neighbors.items():
                neighbor = neighbor_info['node']
                direct_link_dist = neighbor_info['distance']

                # Bellman-Ford equation: new_distance = direct_link + neighbor's known distance to destination
                if dest in neighbor.routing_table:
                    new_distance = direct_link_dist + neighbor.routing_table[dest]
                    
                    # Update if new route is shorter
                    if dest not in self.routing_table or new_distance < self.routing_table[dest]:
                        self.routing_table[dest] = new_distance
                        updated = True
        
        return updated

    def print_routing_table(self):
        """Print the current routing table"""
        print(f"Routing Table for Node {self.name}:")
        for dest, distance in self.routing_table.items():
            print(f"To {dest}: Distance = {distance}")
        print()


