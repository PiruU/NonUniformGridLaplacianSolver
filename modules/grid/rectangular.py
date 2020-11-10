import default
import check
import node
import discretization
import numpy


def make_nodes(
length_x     = default.length_x    ,
length_y     = default.length_y    ,
n_elements_x = default.n_elements_u,
n_elements_y = default.n_elements_v
) :
    """
    Builds an n_elements_x by n_elements_y array of nodes.
    The nodes spread on a length_x by length_y domain.
    """
    builder = make_builder(length_x, length_y, n_elements_x, n_elements_y)
    return builder.nodes()


def make_builder(
length_x     = default.length_x,
length_y     = default.length_y,
n_elements_x = default.n_elements_u,
n_elements_y = default.n_elements_v
) :
    """
    Make an instance of Builder() with given number of elements and dimensions.
    """
    grid_discretization = discretization.make(n_elements_x, n_elements_y)
    dimensions = Dimensions().set_length_x(length_x).set_length_y(length_y)
    return Builder().set_discretization(grid_discretization).set_dimensions(dimensions)


class Builder :
    """
    Class Builder()

    An instance of that class can bu used so as to build an N by M array of nodes that spreads
    on a rectangular shaped domain. Dimensions of the domain can be changed through setters.
    Discretization can also be changed.
    """
    def __init__(self) :
        self._dimensions = Dimensions()
        self._discretization = discretization.Discretization()

    def set_dimensions(self, dimensions) :
        self._dimensions = dimensions
        return self

    def set_discretization(self, discretization) :
        self._discretization = discretization
        return self

    def nodes_positions_x(self) :
        return numpy.linspace(0, self._dimensions.length_x(), self._discretization.count_nodes_u())

    def nodes_positions_y(self) :
        return numpy.linspace(0, self._dimensions.length_y(), self._discretization.count_nodes_v())

    def nodes(self) :
        positions_x = self.nodes_positions_x()
        positions_y = self.nodes_positions_y()
        nodes = [node.make(position_x, position_y) for position_x in positions_x for position_y in positions_y]
        return numpy.reshape(nodes, (self._discretization.count_nodes_u(), self._discretization.count_nodes_v()))


class Dimensions :
    """
    Class Dimension()

    An instance of that class can be used so as to describe a rectangular domain.
    """
    def __init__(self) :
        self._length_x = default.length_x
        self._length_y = default.length_y        

    def set_length_x(self, length) :
        self._length_x = length
        return self

    def set_length_y(self, length) :
        self._length_y = length
        return self

    def length_x(self) :
        return self._length_x

    def length_y(self) :
        return self._length_y

