#!/usr/bin/env python3
import csv
import sys

from astar import AStarSearch
from astar import Graph

def strip_comments_from_file(fp):
    for row in fp:
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

def main(args):
    if len(args) != 4:
        print("Usage: astar.py nodes.csv edges.csv start-node-id goal-node-id")
        sys.exit(1)
    graph = build_graph(args[0], args[1])
    print(f"Graph {graph.node_count()} nodes,  {graph.edge_count()} edges")
    search = AStarSearch(graph)
    path, cost = search.find_path(args[2], args[3])
    print(f"Path = {path}")
    print(f"Cost = {cost}")

if __name__== "__main__":
    # ignore first argument which is just the python file
    main(sys.argv[1:])
