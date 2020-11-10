import os.path
import sys
import pytest
import numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import angle
import angular
import node

def test_make_nodes_x():
    nodes = angular.make_nodes(
    inner_radius     = 1,
    outer_radius     = 3,
    angular_range    = angle.make_degrees(90),
    n_elements_r     = 2,
    n_elements_theta = 2
    )
    tested_coordinates = node.get_nodes_x(nodes)
    expected_coordinates = [
    [0.5 * numpy.sqrt(2), 1, 0.5 * numpy.sqrt(2)],
    [      numpy.sqrt(2), 2,       numpy.sqrt(2)],
    [1.5 * numpy.sqrt(2), 3, 1.5 * numpy.sqrt(2)]
    ]
    return tested_coordinates == expected_coordinates

def test_make_nodes_y():
    nodes = angular.make_nodes(
    inner_radius     = 1,
    outer_radius     = 3,
    angular_range    = angle.make_degrees(90),
    n_elements_r     = 2,
    n_elements_theta = 2
    )
    tested_coordinates = node.get_nodes_y(nodes)
    expected_coordinates = numpy.transpose([
    [-0.5 * numpy.sqrt(2), 1, 0.5 * numpy.sqrt(2)],
    [      -numpy.sqrt(2), 2,       numpy.sqrt(2)],
    [-1.5 * numpy.sqrt(2), 3, 1.5 * numpy.sqrt(2)]
    ])
    return tested_coordinates == expected_coordinates

