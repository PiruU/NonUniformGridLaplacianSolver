import os.path
import sys
import pytest
import numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import rectangular
import node

def test_make_nodes_x():
    n_elements_x, n_elements_y = 10, 5
    nodes = rectangular.make_nodes(
    length_x     = n_elements_x,
    length_y     = n_elements_y,
    n_elements_x = n_elements_x,
    n_elements_y = n_elements_y
    )
    tested_coordinates = node.get_nodes_x(nodes)
    expected_coordinates = [[i] * (n_elements_y + 1) for i in range(n_elements_x + 1)]
    return tested_coordinates == expected_coordinates

def test_make_nodes_y():
    n_elements_x, n_elements_y = 10, 5
    nodes = rectangular.make_nodes(
    length_x     = n_elements_x,
    length_y     = n_elements_y,
    n_elements_x = n_elements_x,
    n_elements_y = n_elements_y
    )
    tested_coordinates = node.get_nodes_y(nodes)
    expected_coordinates = numpy.transpose([[i] * (n_elements_x + 1) for i in range(n_elements_y + 1)])
    return tested_coordinates == expected_coordinates

