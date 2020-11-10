import boundary_condition
import default
import node as nd
import numpy


def count_nodes(nodes) :
    return nd.get_discretization_from_nodes(nodes).count_nodes()


def get_null_sources_vector(nodes) :
    return numpy.zeros(count_nodes(nodes))


def normalize(values) :
    min_value = numpy.min(values)
    delta_values = numpy.max(values) - min_value
    return (values - min_value) / delta_values


class Builder :
    def __init__(self, nodes) :
        self._nodes             = nodes
        self._condition_manager = boundary_condition.Manager()
        self._sources_vector    = get_null_sources_vector(self._nodes)

    def set_boundary_conditions(self, conditions_manager) :
        self._condition_manager = conditions_manager
        return self

    def get(self) :
        for i_condition in range(default.n_conditions) :
             self.update_condition(i_condition)
        return self._sources_vector

    def update_condition(self, i_condition) :
        i_edge_nodes      = Nodes_indices_manager(self._nodes).get_edge(i_condition)
        n_nodes           = len(i_edge_nodes)
        nodes_coordinates = numpy.linspace(0, 1, n_nodes)
        for i_node in range(n_nodes):
             i_edge_node, node_coordinate = i_edge_nodes[i_node], nodes_coordinates[i_node]
             edge_value = self._condition_manager.get_condition(i_condition).value(node_coordinate)
             self._sources_vector[i_edge_node] = edge_value
        return self


class Nodes_indices_manager :
    def __init__(self, nodes) :
        self._discretization = nd.get_discretization_from_nodes(nodes)

    def get_edge(self, i_edge) :
        if i_edge == default.index_north : 
            return self.get_north_edge()
        elif i_edge == default.index_south :
            return self.get_south_edge()
        elif i_edge == default.index_west :
            return self.get_west_edge()
        elif i_edge == default.index_east :
            return self.get_east_edge()
        else :
            return None

    def get_west_edge(self) :
        return numpy.array(range(0, self._discretization.count_nodes_v()))

    def get_east_edge(self) :
        n_nodes   = self._discretization.count_nodes()
        n_nodes_v = self._discretization.count_nodes_v()
        return numpy.array(range(n_nodes - n_nodes_v, n_nodes))

    def get_south_edge(self) :
        n_nodes_u = self._discretization.count_nodes_u()
        n_nodes_v = self._discretization.count_nodes_v()
        return numpy.array(range(0, n_nodes_u)) * n_nodes_v

    def get_north_edge(self) :
        offset_v = self._discretization.count_nodes_v() - 1
        return self.get_south_edge() + offset_v



