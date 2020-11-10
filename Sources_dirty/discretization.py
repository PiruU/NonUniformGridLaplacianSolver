import default


def make(n_elements_u = default.n_elements_u, n_elements_v = default.n_elements_v) :
    """
    Builds an instance of Discretization() by giving the Ou and Ov-wise number of elements.
    """
    return Discretization().set_n_elements_u(n_elements_u).set_n_elements_v(n_elements_v)


def make_from_nodes(nodes) :
    """
    Builds an instance of Discretization() by giving an N by M aray of nodes.
    """
    n_nodes_u, n_nodes_v = nodes.shape
    return make(n_nodes_u - 1, n_nodes_v - 1)


class Discretization :
    """
    class Discretization:
    
    Describes a quadrilateral structured grid discretization.
    The grid has two directions (Ou and Ov).
    """
    def __init__(self) :
        self._n_elements_u = default.n_elements_u
        self._n_elements_v = default.n_elements_v

    def set_n_elements_u(self, n_elements) :
        self._n_elements_u = n_elements
        return self

    def set_n_elements_v(self, n_elements) :
        self._n_elements_v = n_elements
        return self

    def count_elements_u(self) :
        return self._n_elements_u

    def count_elements_v(self) :
        return self._n_elements_v

    def count_nodes_u(self) :
        return self._n_elements_u + 1

    def count_nodes_v(self) :
        return self._n_elements_v + 1

    def count_nodes(self) :
        return self.count_nodes_u() * self.count_nodes_v()

    def count_elements(self) :
        return self.count_elements_u() * self.count_elements_v()

