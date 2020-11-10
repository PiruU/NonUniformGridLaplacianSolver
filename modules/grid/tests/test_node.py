import os.path
import sys
import pytest
import numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import node

def test_make_x():
    tested_node = node.make(1, 2)
    expected_x = 1
    return tested_node.coordinate_x() == expected_x

def test_make_y():
    tested_node = node.make(1, 2)
    expected_y = 2
    return tested_node.coordinate_y() == expected_y

def test_make() :
    tested_node = node.make(1, 2)
    expected_position = [1, 2]
    return tested_node.position() == expected_position

def test_make_nodes_x() :
    tested_nodes_x = node.get_nodes_x(numpy.array([
    [node.make(1, 2), node.make(3, 4)],
    [node.make(5, 6), node.make(7, 8)]]
    ))
    expected_nodes_x = [[1, 3], [5, 7]]
    return tested_nodes_x == expected_nodes_x

def test_make_nodes_y() :
    tested_nodes_y = node.get_nodes_x(numpy.array([
    [node.make(1, 2), node.make(3, 4)],
    [node.make(5, 6), node.make(7, 8)]]
    ))
    expected_nodes_y = [[2, 4], [6, 8]]
    return tested_nodes_y == expected_nodes_y

