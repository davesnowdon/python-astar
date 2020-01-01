import math

class GraphNode(object):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"GraphNode({self.id}, ({self.x}, {self.y})"

class GraphEdge(object):
    def __init__(self, cost, nodes):
        self.cost = cost
        self.nodes = nodes

    def get_destination(self, from_node):
        if self.nodes[0] == from_node:
            return self.nodes[1]
        elif self.nodes[1] == from_node:
            return self.nodes[0]
        else:
            raise IndexError('node not in list')

    def __str__(self):
        return "member of Test"

class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, id, x, y):
        node = GraphNode(id, x, y)
        self.nodes[id] = node

    def get_node(self, id):
        return self.nodes[id]

    def connect_nodes(self, from_node_id, to_node_id, cost):
        fn = self.get_node(from_node_id)
        tn = self.get_node(to_node_id)
        edge = GraphEdge(cost, [fn, tn])
        fn.add_edge(edge)
        tn.add_edge(edge)
        self.edges.append(edge)

    def edge_count(self):
        return len(self.edges)

    def node_count(self):
        return len(self.nodes)

    def heuristic_distance(self, node1_id, node2_id):
        node1 = self.get_node(node1_id)
        node2 = self.get_node(node2_id)
        return math.sqrt((node1.x-node2.x)**2 + (node1.y-node2.y)**2)
