import numpy
import laplacian_matrix
import laplacian_sources_vector

class Solver :
    def __init__(self, nodes) :
        self._matrix = laplacian_matrix.Builder(nodes).get()
        self._sources_vector_builder = laplacian_sources_vector.Builder(nodes)

    def set_nodes(self, nodes) :
        self._nodes = nodes
        return self

    def set_boundary_conditions(self, conditions) :
        self._sources_vector_builder.set_boundary_conditions(conditions)
        return self

    def solve(self) :
        return numpy.linalg.solve(self._matrix, self._sources_vector_builder.get())

