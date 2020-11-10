import numpy as np

def to_radians(angle_degrees) :
    return angle_degrees * np.pi / 180.0


def to_degrees(angle_degrees) :
    return angle_degrees * 180.0 / np.pi


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
