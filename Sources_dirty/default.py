import angle
import boundary_condition

"""
Parameters default values
"""
index_x          = 0
index_y          = 1
index_u          = 0
index_v          = 1
index_uu         = 0
index_vv         = 1
index_uv         = 2
n_conditions     = 4
index_north      = 0
index_south      = 1
index_west       = 2
index_east       = 3
n_elements_u     = 10
n_elements_v     = 10
n_dimensions     = 2
node_position    = [0, 0]
length_x         = 1
length_y         = 1
inner_radius     = 1
outer_radius     = 2
angular_range    = angle.Angle().set_degrees(50)
condition_type   = boundary_condition.make_constant()
position_w       = 0.0
output_file_name = 'output_file.msh'
