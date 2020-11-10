import default
import node as nd
import numpy as np


class First :
    def __init__(self) :
        self._coordinates = []
        self._i_axis = default.index_u

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def set_axis(self, i_axis) :
        self._i_axis = i_axis
        return self

    def get(self) :
        if self._i_axis == default.index_u :
            return First_u().set_coordinates(self._coordinates).get()
        elif self._i_axis == default.index_v :
            return First_v().set_coordinates(self._coordinates).get()
        else :
            return None


class Second :
    def __init__(self) :
        self._coordinates = []
        self._i_axis = default.index_uu

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def set_axis(self, i_axis) :
        self._i_axis = i_axis
        return self

    def get(self) :
        if self._i_axis == default.index_uu :
            return Second_uu().set_coordinates(self._coordinates).get()
        elif self._i_axis == default.index_vv :
            return Second_vv().set_coordinates(self._coordinates).get()
        elif self._i_axis == default.index_uv :
            return Second_uv().set_coordinates(self._coordinates).get()
        else :
            return None


class First_u :
    def __init__(self) :
        self._coordinates = []

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def get(self) :
        return 0.5 * (self._coordinates[2:,1:-1] - self._coordinates[:-2,1:-1])


class First_v :
    def __init__(self) :
        self._coordinates = []

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def get(self) :
        return 0.5 * (self._coordinates[1:-1,2:] - self._coordinates[1:-1,:-2])


class Second_uu :
    def __init__(self) :
        self._coordinates = []

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def get(self) :
        return self._coordinates[2:,1:-1] - 2 * self._coordinates[1:-1,1:-1] + self._coordinates[:-2,1:-1]


class Second_vv :
    def __init__(self) :
        self._coordinates = []

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def get(self) :
        return self._coordinates[1:-1,2:] - 2 * self._coordinates[1:-1,1:-1] + self._coordinates[1:-1,:-2]


class Second_uv :
    def __init__(self) :
        self._coordinates = []

    def set_coordinates(self, coordinates) :
        self._coordinates = coordinates
        return self

    def get(self) :
        return 0.25 * (self._coordinates[2:,2:] + self._coordinates[:-2,:-2] - self._coordinates[:-2,2:] - self._coordinates[2:,:-2])


