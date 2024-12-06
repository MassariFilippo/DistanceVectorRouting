iterations = 5

class Node:
    def __init__(self, name):
        self.name = name
        self.distanceVector = {}
        self.distanceVector[self.name] = 0
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor.name] = {
            'node': neighbor,
            'distance': distance
        }
        self.distanceVector[neighbor.name] = distance

    def update_distanceVector(self):
        updated = False
        for dest, current_dist in list(self.distanceVector.items()):
            # Skip direct neighbors in initial routing
            if dest == self.name:
                continue
            # Check routes through each neighbor
            for neighbor_name, neighbor_info in self.neighbors.items():
                neighbor = neighbor_info['node']
                direct_link_dist = neighbor_info['distance']
                # Bellman-Ford equation: new_distance = direct_link + neighbor's known distance to destination
                if dest in neighbor.distanceVector:
                    new_distance = direct_link_dist + neighbor.distanceVector[dest]
                    # Update if new route is shorter
                    if dest not in self.distanceVector or new_distance < self.distanceVector[dest]:
                        self.distanceVector[dest] = new_distance
                        updated = True
        return updated

    def print_distanceVector(self):
        table = str(self.name)+": "
        for neighbor in self.distanceVector.items():
            table+=str(neighbor)
        print(table)

class RoutingNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def connect_nodes(self, node1, node2, distance):
        node1.add_neighbor(node2, distance)
        node2.add_neighbor(node1, distance)

    def routing_protocol(self, iterations=5):       
        print("--------------- Initial routing tables ---------------")
        for node in self.nodes.values():
            node.print_distanceVector()
        # Routing updates
        for i in range(iterations):
            print("-------------------- Iteration" , i+1, "--------------------")
            updated_nodes = []
            # Collect nodes that updated their routing tables
            for node in self.nodes.values():
                if node.update_distanceVector():
                    updated_nodes.append(node.name)
            print("--------------- Update routing tables ---------------")
            for node_name in updated_nodes:
                self.nodes[node_name].print_distanceVector()

#MAIN

# Create network
network = RoutingNetwork()

# Create nodes
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

# Add nodes to network
network.add_node(A)
network.add_node(B)
network.add_node(C)
network.add_node(D)

# Connect nodes with distances
network.connect_nodes(A, B, 4)
network.connect_nodes(A, C, 2)
network.connect_nodes(B, D, 3)
network.connect_nodes(C, D, 5)

# Run routing simulation
network.routing_protocol(iterations)