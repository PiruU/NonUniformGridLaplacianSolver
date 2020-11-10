
import angular_grid
import boundary_condition
import laplacian
import msh_file

""" generate nodes of an angular grid """
nodes = angular_grid.make_nodes(n_elements_theta = 40, n_elements_r = 20)

""" generates zero valued boundary conditions except at west of the domain (the condition of which has squared sine form) """
conditions = boundary_condition.Manager().set_west_condition(boundary_condition.make_constant(amplitude = 1))

""" builds laplacian solver on defined domain with desired boundary conditions """
laplacian_solver = laplacian.Solver(nodes).set_boundary_conditions(conditions)

""" solves the problem """
solution = laplacian_solver.solve()

""" write corresponding .msh file """
msh_file.Writer().set_nodes(nodes).set_solution(solution).write()

