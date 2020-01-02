import csv
import sys

from astar import Graph

def strip_comments_from_file(fp):
    # iter over readlines() rather than file handle as mock_open does not support iteration
    for row in fp.readlines():
        raw = row.split('#')[0].strip()
        if raw: yield raw

def read_commented_csv(filename):
    """The python CSV module does not handle comments, so we need to filter out comment lines"""
    with open(filename) as csvfile:
        reader = csv.reader(strip_comments_from_file(csvfile))
        return [r for r in reader]

def build_graph(nodes_filename, edges_filename):
    graph = Graph()
    nodes = read_commented_csv(nodes_filename)
    for node_data in nodes:
        node_id = node_data[0]
        node_x = float(node_data[1])
        node_y = float(node_data[2])
        graph.add_node(node_id, node_x, node_y)

    edges = read_commented_csv(edges_filename)
    for edge_data in edges:
        id1 = edge_data[0]
        id2 = edge_data[1]
        cost = float(edge_data[2])
        graph.connect_nodes(id1, id2, cost)
    return graph
