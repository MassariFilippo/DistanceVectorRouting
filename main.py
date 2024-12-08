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
        for neighbor_name, neighbor_info in self.neighbors.items():
            neighbor = neighbor_info['node']
            direct_link_dist = neighbor_info['distance']
            for dest, neighbor_dist in neighbor.distanceVector.items():
                new_distance = direct_link_dist + neighbor_dist
                # Aggiorno il DV con i nuovi nodi scoperti
                if dest not in self.distanceVector:
                    self.distanceVector[dest] = new_distance
                    updated = True
                # Aggiono se la distanza è ridotta
                elif new_distance < self.distanceVector[dest]:
                    self.distanceVector[dest] = new_distance
                    updated = True
        return updated

    def send_distance_vector(self):
        return self.distanceVector

    def print_distanceVector(self):
        table = f"Node {self.name}: "
        for dest in sorted(self.distanceVector.keys()):
            table += f"{dest}({self.distanceVector[dest]}), "
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
            print(f"\n--------------------------- Iterazione: {iteration} ---------------------------")
            # Ogni nodo invia il proprio DV attuale.
            updates = {node.name: node.send_distance_vector() for node in self.nodes.values()}
            any_updates = False
            for node in self.nodes.values():
                # Per ogni nodo, itera sui suoi vicini.
                for neighbor_name, neighbor_info in node.neighbors.items():
                    neighbor = neighbor_info['node']
                    print(f"-------------------------- {node.name} riceve DV({neighbor_name}) ---------------------------")
                    before_update = str(node.distanceVector)
                    # Aggiorna il Distance Vector del nodo basandosi sul DV ricevuto dal vicino.
                    updated = node.update_distanceVector()
                    after_update = str(node.distanceVector)
                    print("------------------------------ Tabella ------------------------------")
                    print(f"{node.name}: {before_update}")
                    print("------------------------- Tabella aggiornata ------------------------")
                    print(f"{node.name}: {after_update}")
                    print("---------------------------------------------------------------------")
                    if updated:
                        any_updates = True
            print("\nTabelle di instradamento dopo l'iterazione")
            for node in self.nodes.values():
                node.print_distanceVector()
            if not any_updates:
                print("\n")
                break

            
# MAIN

# Creazione del network
network = RoutingNetwork()

#Topografia 1
'''
# Creazione dei nodi
A = Node('A')
B = Node('B')
C = Node('C')

# Aggiunta dei nodi alla rete
network.add_node(A)
network.add_node(B)
network.add_node(C)

# Connessioni tra i nodi con le distanze
network.connect_nodes(A, B, 2)
network.connect_nodes(A, C, 2)
network.connect_nodes(A, D, 9)
network.connect_nodes(A, F, 5)
network.connect_nodes(B, D, 3)
'''

#Topografia 2

# Creazione dei nodi
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

# Aggiunta dei nodi alla rete
network.add_node(A)
network.add_node(B)
network.add_node(C)
network.add_node(D)
network.add_node(E)
network.add_node(F)

# Connessioni tra i nodi con le distanze
network.connect_nodes(A, B, 2)
network.connect_nodes(A, C, 2)
network.connect_nodes(A, D, 9)
network.connect_nodes(A, F, 5)
network.connect_nodes(B, D, 3)
network.connect_nodes(C, D, 5)
network.connect_nodes(D, E, 3)
network.connect_nodes(E, C, 1)
network.connect_nodes(E, F, 11)


#Topografia 3
'''
# Creazione dei nodi
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')

# Aggiunta dei nodi alla rete
network.add_node(A)
network.add_node(B)
network.add_node(C)
network.add_node(D)
network.add_node(E)
network.add_node(F)
network.add_node(G)
network.add_node(H)
network.add_node(I)

# Connessioni tra i nodi con le distanze
network.connect_nodes(A, B, 2)
network.connect_nodes(A, C, 2)
network.connect_nodes(A, D, 9)
network.connect_nodes(A, F, 5)
network.connect_nodes(B, D, 3)
network.connect_nodes(C, D, 5)
network.connect_nodes(D, E, 3)
network.connect_nodes(E, C, 1)
network.connect_nodes(E, F, 11)
network.connect_nodes(F, G, 3)
network.connect_nodes(G, E, 4)
network.connect_nodes(H, E, 10)
network.connect_nodes(H, G, 2)
network.connect_nodes(H, D, 2)
network.connect_nodes(I, G, 5)
network.connect_nodes(I, H, 4)
'''

# Avvio del protocollo di routing
network.routing_protocol()
