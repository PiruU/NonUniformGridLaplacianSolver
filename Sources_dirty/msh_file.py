import node as nd
import default
import numpy as np

class Writer :
    def __init__(self) :
        self._file_name = default.output_file_name
        self._nodes = []
        self._solution = []

    def set_file_name(self, file_name) :
        self._file_name = file_name
        return self

    def set_nodes(self, nodes) :
        self._nodes = nodes
        return self

    def set_solution(self, solution) :
        self._solution = solution
        return self

    def write(self) :
        with open(self._file_name, 'w') as result_file :
            Header_writer().set_output_file(result_file).write()
            Nodes_writer().set_nodes(self._nodes).set_output_file(result_file).write()
            Elements_writer().set_nodes(self._nodes).set_output_file(result_file).write()
            Solution_writer().set_nodes(self._nodes).set_solution(self._solution).set_output_file(result_file).write()
        result_file.close()        


class Header_writer :
    def __init__(self) :
        self._output_file = None

    def set_output_file(self, output_file) :
        self._output_file = output_file
        return self

    def write(self) :
        self.write_header().write_mesh_format().write_closure()
        return self

    def write_header(self) :
        self._output_file.write('$MeshFormat\n')
        return self

    def write_mesh_format(self) :
        self._output_file.write('2.2 0 8\n')
        return self

    def write_closure(self) :
        self._output_file.write('$EndMeshFormat\n')
        return self


def get_node_info_str(i_node, node) :
    x_node, y_node, z_node = node.coordinate_u(), node.coordinate_v(), default.position_w
    return np.str(i_node) + ' ' + np.str(x_node) + ' ' + np.str(y_node) + ' ' + np.str(z_node)  + '\n'

class Nodes_writer :
    def __init__(self) :
        self._nodes = []
        self._output_file = None

    def write(self) :
        self.write_header().write_nodes().write_closure()
        return self

    def set_output_file(self, output_file) :
        self._output_file = output_file
        return self

    def set_nodes(self, nodes) :
        self._nodes = np.ravel(nodes)
        return self

    def write_header(self) :
        n_nodes = len(self._nodes)
        self._output_file.write('$Nodes\n')
        self._output_file.write(np.str(n_nodes) + '\n')
        return self

    def write_closure(self) :
        self._output_file.write('$EndNodes\n')
        return self

    def write_nodes(self) :
        n_nodes = len(self._nodes)
        for i_node in range(n_nodes) :
            self._output_file.write(get_node_info_str(i_node, self._nodes[i_node]))
        return self


class Elements_indices_manager :
    def __init__(self) :
        self._discretization = None

    def set_discretization(self, discretization):
        self._discretization = discretization
        return self

    def to_global(self, i_element_u, i_element_v) :
        return i_element_v + i_element_u * self._discretization.count_elements_v()

    def index_u(self, i_global) :
        return i_global // self._discretization.count_elements_v()

    def index_v(self, i_global) :
        return i_global % self._discretization.count_elements_v()
        
    def to_locals(self, i_global) :
        return (self.index_u(i_global), self.index_v(i_global))



class Nodes_indices_manager :
    def __init__(self) :
        self._discretization = None

    def set_discretization(self, discretization):
        self._discretization = discretization
        return self

    def to_global(self, i_node_u, i_node_v) :
        return i_node_v + i_node_u * self._discretization.count_nodes_v()

    def index_u(self, i_global) :
        return i_global // self._discretization.count_nodes_v()

    def index_v(self, i_global) :
        return i_global % self._discretization.count_nodes_v()
        
    def to_locals(self, i_global) :
        return (self.index_u(i_global), self.index_v(i_global))


class Element_manager :
    def __init__(self) :
        self._discretization = None
        self._i_element = None

    def i_nodes(self) :
        return [
            self.i_node_south_west(),
            self.i_node_north_west(),
            self.i_node_north_east(),
            self.i_node_south_east()
        ]

    def set_discretization(self, discretization):
        self._discretization = discretization
        return self

    def set_i_element(self, i_element):
        self._i_element = i_element
        return self

    def i_node_south_west(self) :
        i_element_u, i_element_v = Elements_indices_manager().set_discretization(self._discretization).to_locals(self._i_element)
        return i_element_u * self._discretization.count_nodes_v() + i_element_v

    def i_node_north_west(self) :
        return self.i_node_south_west() + 1

    def i_node_north_east(self) :
        return self.i_node_north_west() + self._discretization.count_nodes_v()

    def i_node_south_east(self) :
        return self.i_node_south_west() + self._discretization.count_nodes_v()


def get_element_info_str(i_element, nodes) :
    [node_1, node_2, node_3, node_4] = nodes
    return np.str(i_element + 1) + ' 3 2 99 2 ' +  np.str(node_1) + ' ' + np.str(node_2) + ' ' + np.str(node_3) + ' ' + np.str(node_4) + '\n'

class Elements_writer :
    def __init__(self) :
        self._output_file = None
        self._discretization = None

    def write(self) :
        self.write_header().write_elements().write_closure()
        return self

    def set_output_file(self, output_file) :
        self._output_file = output_file
        return self

    def set_nodes(self, nodes) :
        self._discretization = nd.get_discretization_from_nodes(nodes)
        return self

    def write_header(self) :
        n_elements = self._discretization.count_elements()
        self._output_file.write('$Elements\n')
        self._output_file.write(np.str(n_elements) + '\n')
        return self

    def write_closure(self) :
        self._output_file.write('$EndElements\n')
        return self

    def write_elements(self) :
        n_elements = self._discretization.count_elements()
        element_manager = Element_manager().set_discretization(self._discretization)
        for i_element in range(n_elements) :
            nodes = element_manager.set_i_element(i_element).i_nodes()
            self._output_file.write(get_element_info_str(i_element, nodes))
        return self


def write_elements(nodes, result_file) :
    n_nodes_x, n_nodes_y = nodes.shape
    n_nodes = n_nodes_x * n_nodes_y
    n_elements = (n_nodes_x - 1) * (n_nodes_y - 1)

    result_file.write('$Elements\n')
    result_file.write(np.str(n_elements) + '\n')
    for i_element_x in range(n_nodes_x - 1) :
        for i_element_y in range(n_nodes_y - 1) :
            i_element = i_element_y + i_element_x * (n_nodes_y - 1)
            i_node_1 = i_element_y + i_element_x * n_nodes_y
            i_node_2 = i_node_1 + 1
            i_node_3 = i_node_2 + n_nodes_y
            i_node_4 = i_node_1 + n_nodes_y
            result_file.write(np.str(i_element + 1) + ' 3 2 99 2 ' + np.str(i_node_1) + ' ' + np.str(i_node_2) + ' ' + np.str(i_node_3) + ' ' + np.str(i_node_4) + '\n')
    result_file.write('$EndElements\n')


class Solution_writer:
    def __init__(self) :
        self._output_file = None
        self._solution = []
        self._n_nodes = 0

    def write(self) :
        self.write_header().write_solution().write_closure()
        return self

    def set_nodes(self, nodes) :
        self._n_nodes = len(np.ravel(nodes))
        return self

    def set_output_file(self, output_file) :
        self._output_file = output_file
        return self

    def set_solution(self, solution) :
        self._solution = solution
        return self

    def write_header(self):
        self._output_file.write('$NodeData\n')
        self._output_file.write('1\n')
        self._output_file.write('\"My data\"\n')
        self._output_file.write('1\n')
        self._output_file.write('0.0\n')
        self._output_file.write('3\n')
        self._output_file.write('0\n')
        self._output_file.write('1\n')
        self._output_file.write(np.str(self._n_nodes) + '\n')
        return self

    def write_solution(self):
        for i_node in range(self._n_nodes) :
            self._output_file.write(np.str(i_node) + ' ' + np.str(self._solution[i_node]) + '\n')
        return self

    def write_closure(self) :
        self._output_file.write('$EndNodeNodes\n')
        return self

