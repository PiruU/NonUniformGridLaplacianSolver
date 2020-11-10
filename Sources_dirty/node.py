import numpy as np
import default
import check
import discretization

def get_discretization_from_nodes(nodes):
    return discretization.make_from_nodes(nodes)

def make(coordinate_x, coordinate_y):
    """
    Create an instance of Node() given its Ox and Oy wise coordinates.
    """
    position = [coordinate_x, coordinate_y]
    return Node().set_position(position)


class Node :
    """
    Class Node:
    
    Container for geometrical nodes. Nodes are located in 2D plane with two axis (Ou and Ov).
    """
    def __init__(self) :
        self._position = np.array(default.node_position)

    def set_position(self, position) :
        if check.has_two_coordinates(position) :
            self._position = np.array([coordinate for coordinate in position])
        return self

    def position(self) :
        return self._position

    def coordinate(self, i_axis) :
        return self._position[i_axis] if check.is_valid_axis_index(i_axis) else None

    def coordinate_x(self) :
        return self._position[default.index_u]

    def coordinate_y(self) :
        return self._position[default.index_v]

    def coordinate_u(self) :
        return float(default.index_u)

    def coordinate_v(self) :
        return float(default.index_v)


def get_nodes_coordinate(nodes, i_axis) :
    """
    Returns an N by M array containing the 'i_axis'-wise coordinate of an N by M array of nodes.
    """
    return np.reshape([node.coordinate(i_axis) for node in np.ravel(nodes)], nodes.shape)


def get_nodes_x(nodes) :
    """
    Returns an N by M array containing the Ox-wise coordinate of an N by M array of nodes.
    """
    return np.reshape([node.coordinate_x() for node in np.ravel(nodes)], nodes.shape)


def get_nodes_y(nodes) :
    """
    Returns an N by M array containing the Oy-wise coordinate of an N by M array of nodes.
    """
    return np.reshape([node.coordinate_y() for node in np.ravel(nodes)], nodes.shape)


