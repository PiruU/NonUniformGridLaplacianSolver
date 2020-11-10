import numpy as np

def make_degrees(value) :
    return Angle().set_degrees(value)

def make_radians(value) :
    return Angle().set_radians(value)

def to_radians(value_degrees) :
    return value_degrees * np.pi / 180.0

def to_degrees(value_radians) :
    return value_radians * 180.0 / np.pi

class Angle :
    def __init__(self) :
        self._value = 0

    def set_degrees(self, value) :
        self._value = to_radians(value)
        return self

    def set_radians(self, value) :
        self._value = value
        return self

    def degrees(self) :
        return to_degrees(self._value)

    def radians(self) :
        return self._value

