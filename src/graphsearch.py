#!/usr/bin/env python3
import argparse
import sys

from astar import AStarSearch, Graph, build_graph

def main():
    parser = argparse.ArgumentParser(description="Use A* search to find the optimal path between two nodes on the graph")
    parser.add_argument("nodes_filename", help="File containing node data in CSV format")
    parser.add_argument("edges_filename", help="File containing edge data in CSV format")
    parser.add_argument("start_node_id", help="ID of node to start search")
    parser.add_argument("goal_node_id", help="ID of node to find path to")
    parser.add_argument("-o", "--output", help="Write path to this file as comma separated list of node IDs")
    args = parser.parse_args()

    graph = build_graph(args.nodes_filename, args.edges_filename)
    print(f"Graph {graph.node_count()} nodes,  {graph.edge_count()} edges")
    search = AStarSearch(graph)
    path, cost = search.find_path(args.start_node_id, args.goal_node_id)
    print(f"Path = {path}")
    print(f"Cost = {cost}")

    if args.output:
        with open(args.output, "w") as outfile:
            node_ids = [node.id for node in path]
            data = ",".join(node_ids)
            outfile.write(data)

if __name__== "__main__":
    main()
