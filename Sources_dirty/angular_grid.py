import default
import grid
import node as nd
import numpy as np

class Dimensions :
    def __init__(self) :
        self._inner_radius  = default.inner_radius
        self._outer_radius  = default.outer_radius
        self._angular_range = default.angular_range

    def set_inner_radius(self, radius) :
        self._inner_radius = radius
        return self

    def set_outer_radius(self, radius) :
        self._outer_radius = radius
        return self

    def set_angular_range(self, angular_range) :
        self._angular_range = angular_range
        return self

    def inner_radius(self) :
        return self._inner_radius

    def outer_radius(self) :
        return self._outer_radius

    def angular_range(self) :
        return self._angular_range


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

    def nodes_positions_r(self) :
        inner_radius = self._dimensions.inner_radius()
        outer_radius = self._dimensions.outer_radius()
        n_nodes_r = self._discretization.count_nodes_u()
        return np.linspace(inner_radius, outer_radius, n_nodes_r)

    def nodes_positions_theta(self) :
        half_angular_range = self._dimensions.angular_range().radians()
        n_nodes_theta = self._discretization.count_nodes_v()
        return np.linspace(-half_angular_range, half_angular_range, n_nodes_theta)

    def nodes_positions_x(self) :
        positions_r     = self.nodes_positions_r()
        positions_theta = self.nodes_positions_theta()
        return [position_r * np.cos(position_theta) for position_r in positions_r for position_theta in positions_theta]

    def nodes_positions_y(self) :
        positions_r     = self.nodes_positions_r()
        positions_theta = self.nodes_positions_theta()
        return [position_r * np.sin(position_theta) for position_r in positions_r for position_theta in positions_theta]

    def nodes(self) :
        positions_xy = zip(self.nodes_positions_x(), self.nodes_positions_y())
        nodes = [nd.Node().set_position([position_x, position_y]) for (position_x, position_y) in positions_xy]
        return np.reshape(nodes, (self._discretization.count_nodes_u(), self._discretization.count_nodes_v()))


def make_dimensions(
inner_radius  = default.inner_radius,
outer_radius  = default.outer_radius,
angular_range = default.angular_range
) :
    return Dimensions().set_inner_radius(inner_radius).set_outer_radius(outer_radius).set_angular_range(angular_range)


def make_nodes(
inner_radius     = default.inner_radius,
outer_radius     = default.outer_radius,
angular_range    = default.angular_range,
n_elements_r     = default.n_elements_u,
n_elements_theta = default.n_elements_v
) :
    discretization = grid.make_discretization(n_elements_r, n_elements_theta)
    dimensions     = make_dimensions(inner_radius, outer_radius, angular_range)
    return nodes_builder().set_discretization(discretization).set_dimensions(dimensions).nodes()



