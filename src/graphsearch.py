#!/usr/bin/env python3
import argparse
import csv
import sys

from astar import AStarSearch, Graph, build_graph

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
