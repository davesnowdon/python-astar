import unittest
from unittest.mock import patch, mock_open

from astar import build_graph, read_commented_csv

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

nodes_file_content_with_comments ="""# comment 1
    # comment 2
    99,-0.5,-0.5,1.4142
    """ + nodes_file_content

edges_file_content_with_comments="""# edges.csv file for V-REP kilobot motion planning scene.
    # All lines beginning with a # are treated as a comment and ignored.
    # Each line below is of the form
    # ID1,ID2,cost
    # where ID1 and ID2 are the IDs of the nodes connected by the edge and
    # cost is the cost of traversing that edge (in either direction).
    12,11,0.214
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

def test_read_commented_csv_returns_all_lines_if_no_comments():
    # python 2.7
    #with patch('__builtin__.open', mock_handle):
    with patch('builtins.open', mock_open(read_data=nodes_file_content)) as mock_file:
        result = read_commented_csv("no-comments.csv")
        assert len(result) ==  12
        mock_file.assert_called_with("no-comments.csv")

def test_read_commented_csv_skips_comments():
    with patch('builtins.open', mock_open(read_data=nodes_file_content_with_comments)) as mock_file:
        result = read_commented_csv("comments.csv")
        assert len(result) ==  13
        mock_file.assert_called_with("comments.csv")

def test_read_commented_csv_handles_edges_file():
    with patch('builtins.open', mock_open(read_data=edges_file_content_with_comments)) as mock_file:
        result = read_commented_csv("edges.csv")
        assert len(result) ==  19
        mock_file.assert_called_with("edges.csv")

def test_build_graph_handles_example_data():
    # this relies on the nodes file being read before the edges file
    # see https://stackoverflow.com/questions/25555161/mock-builtin-open-function-when-used-in-contextlib/27160842#27160842
    # less assumptions, but more boilerplate
    # https://stackoverflow.com/questions/34423564/how-to-mock-open-differently-depending-on-the-parameters-passed-to-open
    mock_nodes = mock_open(read_data=nodes_file_content)
    mock_edges = mock_open(read_data=edges_file_content_with_comments)
    mock_nodes.side_effect=[mock_nodes.return_value, mock_edges.return_value]
    with patch('builtins.open', mock_nodes):
        graph = build_graph("fake nodes.csv", "fake edges.csv")
        assert graph.node_count() == 12
        assert graph.edge_count() == 19
