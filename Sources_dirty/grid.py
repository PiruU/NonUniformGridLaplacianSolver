import default

class Discretization :
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


def make_discretization(n_elements_x = default.n_elements_u, n_elements_y = default.n_elements_v) :
    return Discretization().set_n_elements_u(n_elements_x).set_n_elements_v(n_elements_y)


