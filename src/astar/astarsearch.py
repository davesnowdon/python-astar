#!/usr/bin/env python3
import csv
import sys
import math

from astar import PriorityQueue

class AStarSearch(object):
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start_node_id, goal_node_id):
        self.open_nodes = PriorityQueue()
        self.closed_nodes = []
        self.parents = {}
        self.costs = {}

        start_node = self.graph.get_node(start_node_id)
        self.open_nodes.add(0, start_node)
        self.costs[start_node.id] = 0

        while len(self.open_nodes) > 0:
            cur_node = self.open_nodes.pop()
            if cur_node.id == goal_node_id:
                return self.reconstruct_path(start_node, cur_node)
            for edge in cur_node.edges:
                edge_node = edge.get_destination(cur_node)
                if edge_node in self.closed_nodes:
                    continue

                cost_to_get_here = self.costs[cur_node.id] + edge.cost
                if self.cheaper_cost(edge_node.id, cost_to_get_here):
                    self.parents[edge_node.id] = cur_node.id
                    self.costs[edge_node.id] = cost_to_get_here
                    estimated_cost = self.graph.heuristic_distance(edge_node.id, goal_node_id)
                    f = cost_to_get_here + estimated_cost
                    self.open_nodes.add_update(f, edge_node)

            self.closed_nodes.append(cur_node)
        # failed to find path, nothing left in open list
        return None

    def reconstruct_path(self, start_node, end_node):
        path = [end_node]
        cur_node = end_node
        while cur_node != start_node:
            next_id = self.parents[cur_node.id]
            cur_node = self.graph.get_node(next_id)
            path = [cur_node] + path
        return path

    def cheaper_cost(self, node_id, cost):
        cur_cost = self.costs.get(node_id, sys.float_info.max)
        return cost < cur_cost
