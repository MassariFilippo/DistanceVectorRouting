class Node:
    def __init__(self, name):
        self.name = name
        self.distanceVector = {self.name: 0}
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
            for neighbor_name, neighbor_info in self.neighbors.items():
                neighbor = neighbor_info['node']
                direct_link_dist = neighbor_info['distance']
                if dest in neighbor.distanceVector:
                    new_distance = direct_link_dist + neighbor.distanceVector[dest]
                    if dest not in self.distanceVector or new_distance < self.distanceVector[dest]:
                        self.distanceVector[dest] = new_distance
                        updated = True
        return updated

    def send_distance_vector(self):
        return self.distanceVector

    def print_distanceVector(self):
        table = f"Node {self.name}: "
        for dest, dist in self.distanceVector.items():
            table += f"{dest}({dist}), "
        print(table)


class RoutingNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def connect_nodes(self, node1, node2, distance):
        node1.add_neighbor(node2, distance)
        node2.add_neighbor(node1, distance)

    def routing_protocol(self):
        iteration = 0
        while True:
            iteration += 1
            print(f"\nIterazione: {iteration}")

            updates = {node.name: node.send_distance_vector() for node in self.nodes.values()}
            any_updates = False

            for node in self.nodes.values():
                for neighbor_name, neighbor_info in node.neighbors.items():
                    neighbor = neighbor_info['node']
                    print(f"-------------------------- {node.name} riceve DV({neighbor_name}) ---------------------------")
                    before_update = str(node.distanceVector)
                    updated = node.update_distanceVector()
                    after_update = str(node.distanceVector)
                    print("------------------------------ Tabella ------------------------------")
                    print(f"{node.name}: {before_update}")
                    print("------------------------- Tabella aggiornata ------------------------")
                    print(f"{node.name}: {after_update}")
                    print("---------------------------------------------------------------------")
                    if updated:
                        any_updates = True
            
            print("\nTabelle di instradamento dopo l'iterazione:")
            for node in self.nodes.values():
                node.print_distanceVector()

            if not any_updates:
                print("\nNessun aggiornamento necessario")
                break

# MAIN

# Creazione del network
network = RoutingNetwork()

# Creazione dei nodi
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

# Aggiunta dei nodi alla rete
network.add_node(A)
network.add_node(B)
network.add_node(C)
network.add_node(D)

# Connessioni tra i nodi con le distanze
network.connect_nodes(A, B, 2)
network.connect_nodes(A, C, 2)
network.connect_nodes(B, D, 3)
network.connect_nodes(C, D, 5)

# Avvio del protocollo di routing
network.routing_protocol()
