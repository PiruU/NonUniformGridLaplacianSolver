import numpy
import node
import mathematical_model

def get_pattern_length(nodes) :
    return 2 * node.get_discretization_from_nodes(nodes).count_nodes_v() + 3


def initialize_null_pattern(nodes) :
    n_diagonals = get_pattern_length(nodes)
    return numpy.zeros(n_diagonals)


class Builder :
    def __init__(self, nodes) :
        self._pattern         = initialize_null_pattern(nodes)
        self._coupling_terms  = Coupling_terms_manager(nodes)
        self._indices         = Indices_manager(nodes)

    def set_i_node_u(self, i_node_u) :
        self._i_node_u = i_node_u
        return self

    def set_i_node_v(self, i_node_v) :
        self._i_node_v = i_node_v
        return self

    def get(self) :
        self.update_south_west_node_term().update_west_node_term().update_north_west_node_term()
        self.update_south_node_term().update_central_node_term().update_north_node_term()
        self.update_south_east_node_term().update_east_node_term().update_north_east_node_term()
        return self._pattern

    def update_south_west_node_term(self) :
        gammas = self._coupling_terms.get_gammas()
        self._pattern[self._indices.south_west()] = 0.5 * gammas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_west_node_term(self) :
        alphas, deltas = self._coupling_terms.get_alphas(), self._coupling_terms.get_deltas()
        self._pattern[self._indices.west()] = alphas[self._i_node_u - 1, self._i_node_v - 1] - 0.5 * deltas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_north_west_node_term(self) :
        gammas = self._coupling_terms.get_gammas()
        self._pattern[self._indices.north_west()] = -0.5 * gammas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_south_node_term(self) :
        betas, etas = self._coupling_terms.get_betas(), self._coupling_terms.get_etas()
        self._pattern[self._indices.south()] = betas[self._i_node_u - 1, self._i_node_v - 1] - 0.5 * etas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_central_node_term(self) :
        alphas, betas = self._coupling_terms.get_alphas(), self._coupling_terms.get_betas()
        self._pattern[self._indices.central()] = -2 * (alphas[self._i_node_u - 1, self._i_node_v - 1] + betas[self._i_node_u - 1, self._i_node_v - 1])
        return self

    def update_north_node_term(self) :
        betas, etas = self._coupling_terms.get_betas(), self._coupling_terms.get_etas()
        self._pattern[self._indices.north()] = betas[self._i_node_u - 1, self._i_node_v - 1] + 0.5 * etas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_south_east_node_term(self) :
        gammas = self._coupling_terms.get_gammas()
        self._pattern[self._indices.south_east()] = -0.5 * gammas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_east_node_term(self) :
        alphas, deltas = self._coupling_terms.get_alphas(), self._coupling_terms.get_deltas()
        self._pattern[self._indices.east()] = alphas[self._i_node_u - 1, self._i_node_v - 1] + 0.5 * deltas[self._i_node_u - 1, self._i_node_v - 1]
        return self

    def update_north_east_node_term(self) :
        gammas = self._coupling_terms.get_gammas()
        self._pattern[self._indices.north_east()] = 0.5 * gammas[self._i_node_u - 1, self._i_node_v - 1]
        return self


class Indices_manager :
    def __init__(self, nodes) :
        self._discretization = node.get_discretization_from_nodes(nodes)

    def central(self) :
        return self._discretization.count_nodes_v() + 1

    def north(self) :
        return self.central() + 1

    def south(self) :
        return self.central() - 1

    def east(self) :
        return self.central() + self._discretization.count_nodes_v()

    def west(self) :
        return self.central() - self._discretization.count_nodes_v()

    def south_west(self) :
        return self.west() - 1

    def north_west(self) :
        return self.west() + 1

    def south_east(self) :
        return self.east() - 1

    def north_east(self) :
        return self.east() + 1


class Coupling_terms_manager :
    def __init__(self, nodes) :
        self._alphas = mathematical_model.get_alphas_terms(nodes)
        self._betas  = mathematical_model.get_betas_terms(nodes)
        self._gammas = mathematical_model.get_gammas_terms(nodes)
        self._deltas = mathematical_model.get_deltas_terms(nodes)
        self._etas   = mathematical_model.get_etas_terms(nodes)

    def get_alphas(self) :
        return self._alphas

    def get_betas(self) :
        return self._betas

    def get_gammas(self) :
        return self._gammas

    def get_deltas(self) :
        return self._deltas

    def get_etas(self) :
        return self._etas

