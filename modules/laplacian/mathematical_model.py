import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..\grid'))

import default
import derivative
import node

"""
Functions in this file are related to the finite-diference expression of the laplacian.
These functions cannot be explained or cannot be assigned a signification. They are just
derivatives terms appearing in the formulation of the coefficients of the laplacian matrix..
Formulations of the problem can be found in the technical documentation (folder ./doc/)
"""
def get_xu_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_x)
    return derivative.First().set_coordinates(nodes_coordinates).set_axis(default.index_u).get()

def get_yu_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_y)
    return derivative.First().set_coordinates(nodes_coordinates).set_axis(default.index_u).get()

def get_xv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_x)
    return derivative.First().set_coordinates(nodes_coordinates).set_axis(default.index_v).get()

def get_yv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_y)
    return derivative.First().set_coordinates(nodes_coordinates).set_axis(default.index_v).get()

def get_xuu_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_x)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_uu).get()

def get_xvv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_x)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_vv).get()

def get_xuv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_x)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_uv).get()

def get_yuu_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_y)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_uu).get()

def get_yvv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_y)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_vv).get()

def get_yuv_terms(nodes) :
    nodes_coordinates = node.get_nodes_coordinate(nodes, default.index_y)
    return derivative.Second().set_coordinates(nodes_coordinates).set_axis(default.index_uv).get()

def get_as_terms(nodes) :
    return get_xv_terms(nodes)**2 + get_yv_terms(nodes)**2

def get_bs_terms(nodes) :
    return get_xu_terms(nodes)**2 + get_yu_terms(nodes)**2

def get_cs_terms(nodes) :
    return get_xu_terms(nodes) * get_xv_terms(nodes) + get_yu_terms(nodes) * get_yv_terms(nodes)

def get_ds_terms(nodes) :
    return get_xv_terms(nodes) * get_yu_terms(nodes) - get_xu_terms(nodes) * get_yv_terms(nodes)

def get_alphas_terms(nodes) :
    return get_as_terms(nodes) / get_ds_terms(nodes)**2

def get_betas_terms(nodes) :
    return get_bs_terms(nodes) / get_ds_terms(nodes)**2

def get_gammas_terms(nodes) :
    return -get_cs_terms(nodes) / get_ds_terms(nodes)**2

def get_deltas_terms(nodes) :
    return (
    get_as_terms(nodes)     * (get_xuu_terms(nodes) * get_yv_terms(nodes) - get_yuu_terms(nodes) * get_xv_terms(nodes)) +
    get_bs_terms(nodes)     * (get_xvv_terms(nodes) * get_yv_terms(nodes) - get_yvv_terms(nodes) * get_xv_terms(nodes)) +
    get_cs_terms(nodes) * 2 * (get_yuv_terms(nodes) * get_xv_terms(nodes) - get_xuv_terms(nodes) * get_yv_terms(nodes))
    ) / get_ds_terms(nodes)**3

def get_etas_terms(nodes) :
    return (
    get_as_terms(nodes) *     (get_yuu_terms(nodes) * get_xu_terms(nodes) - get_xuu_terms(nodes) * get_yu_terms(nodes)) +
    get_bs_terms(nodes) *     (get_yvv_terms(nodes) * get_xu_terms(nodes) - get_xvv_terms(nodes) * get_yu_terms(nodes)) +
    get_cs_terms(nodes) * 2 * (get_yu_terms(nodes) * get_xuv_terms(nodes) - get_xu_terms(nodes) * get_yuv_terms(nodes))
    ) / get_ds_terms(nodes)**3

