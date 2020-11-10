import numpy as np

default_params = { 'amplitude' : 1 }
def constant(coordinate, params = default_params) :
    return params['amplitude']


def sine(coordinate, params = default_params) :
    return params['amplitude'] * np.sin(2 * np.pi * coordinate)


def cosine(coordinate, params = default_params) :
    return params['amplitude'] * np.cos(2 * np.pi * coordinate)


def squared_sine(coordinate, params = default_params) :
    return params['amplitude'] * np.sin(np.pi * coordinate)**2


def squared_cosine(coordinate, params = default_params) :
    return params['amplitude'] * np.cos(np.pi * coordinate)**2

