import os.path
import sys
import pytest
import numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import node
import discretization

def test_make_n_elements_u() :
    tested_n_elements_u = discretization.make(n_elements_u = 10).count_elements_u()
    expected_n_elements_u = 10
    return tested_n_elements_u == expected_n_elements_u

def test_make_n_elements_v() :
    tested_n_elements_v = discretization.make(n_elements_v = 5).count_elements_v()
    expected_n_elements_v = 5
    return tested_n_elements_v == expected_n_elements_v

def test_make_n_nodes_u() :
    tested_n_nodes_u = discretization.make(n_elements_u = 5).count_nodes_u()
    expected_n_nodes_u = 6
    return tested_n_nodes_u == expected_n_nodes_u

def test_make_n_nodes_u() :
    tested_n_nodes_v = discretization.make(n_elements_v = 10).count_nodes_v()
    expected_n_nodes_v = 11
    return tested_n_nodes_v == expected_n_nodes_v

def test_make_n_elements() :
    tested_n_elements = discretization.make(n_elements_u = 10, n_elements_v = 5).count_elements()
    expected_n_elements = 50
    return tested_n_elements == expected_n_elements

def test_make_n_nodes() :
    tested_n_nodes = discretization.make(n_elements_u = 10, n_elements_v = 5).count_nodes()
    expected_n_nodes = 66
    return tested_n_nodes == expected_n_nodes

def test_make_from_nodes_n_elements_u() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_elements_u = discretization.make_from_nodes(nodes).count_elements_u()
    expected_n_elements_u = 6
    return tested_n_elements_u == expected_n_elements_u

def test_make_from_nodes_n_elements_v() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_elements_v = discretization.make_from_nodes(nodes).count_elements_v()
    expected_n_elements_v = 3
    return tested_n_elements_v == expected_n_elements_v

def test_make_from_nodes_n_elements() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_elements = discretization.make_from_nodes(nodes).count_elements()
    expected_n_elements = 18
    return tested_n_elements == expected_n_elements

def test_make_from_nodes_n_nodes_u() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_nodes_u = discretization.make_from_nodes(nodes).count_nodes_u()
    expected_n_nodes_u = 7
    return tested_n_nodes_u == expected_n_nodes_u

def test_make_from_nodes_n_nodes_v() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_nodes_v = discretization.make_from_nodes(nodes).count_nodes_v()
    expected_n_nodes_v = 4
    return tested_n_nodes_v == expected_n_nodes_v

def test_make_from_nodes_n_nodes() :
    nodes = numpy.array([[node.make(0, 0)] * 4] * 7)
    tested_n_nodes = discretization.make_from_nodes(nodes).count_nodes()
    expected_n_nodes = 28
    return tested_n_nodes == expected_n_nodes
 
