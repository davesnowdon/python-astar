import unittest
from unittest.mock import patch, mock_open

from astar import Graph, AStarSearch, build_graph

nodes_file_content ="""1,-0.5,-0.5,1.4142
    2,-0.09,-0.4,1.0762
    3,-0.285,-0.305,1.1244
    4,0.0575,-0.225,0.8494
    5,-0.0525,-0.0175,0.7604
    6,-0.37,0.3,0.8927
    7,0.3525,-0.0525,0.5719
    8,0.0625,0.255,0.5014
    9,-0.1,0.3725,0.6134
    10,0.4275,0.195,0.3135
    11,0.345,0.3525,0.214
    12,0.5,0.5,0"""

edges_file_content = """12,11,0.214
    12,10,0.3135
    12,8,0.5014
    11,10,0.1778
    11,9,0.4454
    10,7,0.2586
    9,8,0.2005
    9,6,0.2796
    9,5,0.5994
    8,4,0.48
    7,4,0.3417
    5,2,0.179
    4,3,0.3517
    4,2,0.2289
    3,2,0.2169
    3,1,0.2903
    2,1,0.422
    7,5,0.4402
    5,4,0.11"""

def build_graph_from_example_data():
    mock_nodes = mock_open(read_data=nodes_file_content)
    mock_edges = mock_open(read_data=edges_file_content)
    mock_nodes.side_effect=[mock_nodes.return_value, mock_edges.return_value]
    with patch('builtins.open', mock_nodes):
        return build_graph("fake nodes.csv", "fake edges.csv")

def test_start_goal_same_returns_path_with_one_item():
    graph = build_graph_from_example_data()
    search = AStarSearch(graph)
    path, _ = search.find_path("1", "1")
    assert len(path) == 1

def test_start_goal_neighbours_returns_two_item_path():
    graph = build_graph_from_example_data()
    search = AStarSearch(graph)
    path, _ = search.find_path("1", "2")
    assert len(path) == 2

def test_finds_least_cost_path():
    graph = build_graph_from_example_data()
    search = AStarSearch(graph)
    path, _ = search.find_path("1", "6")
    assert len(path) == 5
