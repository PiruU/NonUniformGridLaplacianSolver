import os.path
import sys
import numpy

sys.path.append(os.path.join(os.path.dirname(__file__), '..\grid'))

import discretization

"""
import default
import derivative
import node as nd
import laplacian_pattern
"""

class Builder :
    def __init__(self, nodes) :
        self._nodes = nodes
        self._discretization = discretization.make_from_nodes(self._nodes)

    def get(self) :
        n_nodes_u = self._discretization.count_nodes_u()
        n_nodes_v = self._discretization.count_nodes_v()
        matrix = numpy.eye(self._discretization.count_nodes())
        inner_node_builder = laplacian_pattern.Builder(self._nodes)
        for i_node_u in range(1, self._discretization.count_nodes_u() - 1) :
            for i_node_v in range(1, self._discretization.count_nodes_v() - 1) :
                ij_node = Nodes_indices_manager(self._nodes).i_node_global(i_node_u, i_node_v)
                pattern = inner_node_builder.set_i_node_u(i_node_u).set_i_node_v(i_node_v).get()
                matrix[ij_node,ij_node - n_nodes_v - 1:ij_node + n_nodes_v + 2] = pattern
        return matrix


class Nodes_indices_manager :
    def __init__(self, nodes) :
        self._discretization = nd.get_discretization_from_nodes(nodes)

    def i_node_global(self, i_node_u, i_node_v) :
        return i_node_v + i_node_u * self._discretization.count_nodes_v()

    def i_node_v(self, i_global) :
        return i_global % self._discretization.count_nodes_v()

    def i_node_u(self, i_global) :
        return i_global // self._discretization.count_nodes_v()

    def i_node_locals(self, i_global) :
        return (self.i_node_u(i_global), self.i_node_v(i_global))


class Nodes_edges_checker :
    def __init__(self, nodes) :
        self._discretization  = nd.get_discretization_from_nodes(nodes)
        self._node = Nodes_indices_manager(self._discretization)

    def is_on_left_edge(self, i_node_global) :
        return self._node.i_node_u(i_node_global) == 0

    def is_on_bottom_edge(self, i_node_global) :
        return self._node.i_node_v(i_node_global) == 0

    def is_on_top_edge(self, i_node_global) :
        return self._node.i_node_u(i_node_global) == self._discretization.count_nodes_u()

    def is_on_right_edge(self, i_node_global) :
        return self._node.i_node_v(i_node_global) == self._discretization.count_nodes_v()

    def is_on_edge(self, i_global) :
        return self._node.is_on_bottom_edge() or self._node.is_on_left_edge() or self._node.is_on_right_edge() or self._node.is_on_top_edge()


