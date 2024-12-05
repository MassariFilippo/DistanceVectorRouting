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


class RoutingNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        """Add a node to the network"""
        self.nodes[node.name] = node

    def connect_nodes(self, node1, node2, distance):
        """Connect two nodes with a specific distance"""
        node1.add_neighbor(node2, distance)
        node2.add_neighbor(node1, distance)

    def run_routing_protocol(self, iterations=5):
        """Simulate routing protocol updates"""
        print("Running Distance Vector Routing Simulation\n")
        
        # Initial routing tables
        for node in self.nodes.values():
            node.print_routing_table()

        # Perform routing updates
        for i in range(iterations):
            print(f"\nIteration {i + 1}:")
            updated_nodes = []
            
            # Collect nodes that updated their routing tables
            for node in self.nodes.values():
                if node.update_routing_table():
                    updated_nodes.append(node.name)
            
            # Print updated routing tables
            for node_name in updated_nodes:
                self.nodes[node_name].print_routing_table()

