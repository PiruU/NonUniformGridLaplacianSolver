import default
import check
import node as nd
import boundary_condition
import grid
import numpy as np

class Dimensions :
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


class boundary_conditions :
    """
    """
    def __init__(self) :
        self._description = {
        default.top_tag    : boundary_condition.Constant().set_amplitude(0.0),
        default.bottom_tag : boundary_condition.Constant().set_amplitude(0.0),
        default.left_tag   : boundary_condition.Constant().set_amplitude(0.0),
        default.right_tag  : boundary_condition.Constant().set_amplitude(0.0)
        }

    def set_top(self, boundary_condition) :
        self._description[default.top_tag] = boundary_condition
        return self

    def set_bottom(self, boundary_condition) :
        self._description[default.bottom_tag] = boundary_condition
        return self

    def set_left(self, boundary_condition) :
        self._description[default.left_tag] = boundary_condition
        return self

    def set_right(self, boundary_condition) :
        self._description[default.right_tag] = boundary_condition
        return self

    def get_top(self, boundary_condition) :
        return self._description[default.top_tag]

    def get_bottom(self, boundary_condition) :
        return self._description[default.bottom_tag]

    def get_left(self, boundary_condition) :
        return self._description[default.left_tag]

    def get_right(self, boundary_condition) :
        return self._description[default.right_tag]


class nodes_builder :
    def __init__(self) :
        self._dimensions = Dimensions()
        self._discretization = grid.Discretization()

    def set_dimensions(self, dimensions) :
        self._dimensions = dimensions
        return self

    def set_discretization(self, discretization) :
        self._discretization = discretization
        return self

    def nodes_positions_x(self) :
        return np.linspace(0, self._dimensions.length_x(), self._discretization.count_nodes_u())

    def nodes_positions_y(self) :
        return np.linspace(0, self._dimensions.length_y(), self._discretization.count_nodes_v())

    def nodes(self) :
        positions_x = self.nodes_positions_x()
        positions_y = self.nodes_positions_y()
        nodes = [nd.Node().set_position([position_x, position_y]) for position_x in positions_x for position_y in positions_y]
        return np.reshape(nodes, (self._discretization.count_nodes_u(), self._discretization.count_nodes_v()))


def make_dimensions(length_x = default.length_x, length_y = default.length_y) :
    return Dimensions().set_length_x(length_x).set_length_y(length_y)

def make_nodes(length_x = default.length_x, length_y = default.length_y, n_elements_x = default.n_elements_u, n_elements_y = default.n_elements_v) :
    discretization = grid.make_discretization(n_elements_x, n_elements_y)
    dimensions = make_dimensions(length_x, length_y)
    return nodes_builder().set_discretization(discretization).set_dimensions(dimensions).nodes()

