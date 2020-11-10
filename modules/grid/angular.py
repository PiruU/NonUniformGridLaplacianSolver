import default
import discretization
import node as nd
import numpy as np

def make_nodes(
inner_radius     = default.inner_radius,
outer_radius     = default.outer_radius,
angular_range    = default.angular_range,
n_elements_r     = default.n_elements_u,
n_elements_theta = default.n_elements_v
) :
    """
    Builds an n_elements_r by n_elements_theta array of nodes.
    The nodes spread on an angular domain with 'angular_range' and 'inner_radius - outer_radius' sizes.
    """
    builder = make_builder(inner_radius, outer_radius, angular_range, n_elements_r, n_elements_theta)
    return builder.nodes()


def make_builder(
inner_radius     = default.inner_radius,
outer_radius     = default.outer_radius,
angular_range    = default.angular_range,
n_elements_r     = default.n_elements_u,
n_elements_theta = default.n_elements_v
) :
    """
    Make an instance of Builder() with given number of elements and dimensions.
    """
    grid_discretization = discretization.make(n_elements_r, n_elements_theta)
    dimensions = make_dimensions(inner_radius, outer_radius, angular_range)
    return Builder().set_discretization(grid_discretization).set_dimensions(dimensions)


def make_dimensions(
inner_radius  = default.inner_radius,
outer_radius  = default.outer_radius,
angular_range = default.angular_range
) :
    """
    Make an instance of Dimension() with given parameters values.
    """
    return Dimensions().set_inner_radius(inner_radius).set_outer_radius(outer_radius).set_angular_range(angular_range)


class Builder :
    """
    Class Builder()

    An instance of that class can bu used so as to build an N by M array of nodes that spreads
    on an angular shaped domain. Dimensions of the domain can be changed through setters.
    Discretization can also be changed.
    """
    def __init__(self) :
        self._dimensions = Dimensions()
        self._discretization = discretization.make()

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


class Dimensions :
    """
    Class Dimension()

    An instance of that class can be used so as to describe an angular domain.
    """
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

