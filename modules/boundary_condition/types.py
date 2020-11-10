import check
import function

def make_constant(amplitude = 0) :
    """ Returns a constant-type boundary condition """
    return Constant().set_amplitude(amplitude)

def make_squared_sine(amplitude = 1) :
    """ Returns a squared sine-type boundary condition """
    return Squared_sine().set_amplitude(amplitude)

def make_squared_cosine(amplitude = 1) :
    """ Returns a squared cosine-type boundary condition """
    return Squared_cosine().set_amplitude(amplitude)

def make_sine(amplitude = 1) :
    """ Returns a sine-type boundary condition """
    return Sine().set_amplitude(amplitude)

def make_cosine(amplitude = 1) :
    """ Returns a cosine-type boundary condition """
    return Cosine().set_amplitude(amplitude)


class Custom :
    """
    class Custom:

    Describes a boundary condition with custom user-defined base function.
    """
    def __init__(self) :
        self._function = function.constant
        self._params   = function.default_params

    def set_function(self, function) :
        self._function = function
        return self

    def set_params(self, params) :
        self._params = params
        return self

    def value(self, coordinate) :
        return self._function(coordinate, self._params) if check.is_in_unit_segment(coordinate) else 0.0


class Constant :
    """
    class Custom:

    Describes a boundary condition with constant base function.
    """
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.constant).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Sine :
    """
    class Custom:

    Describes a boundary condition with sine base function.
    """
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.sine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Cosine :
    """
    class Custom:

    Describes a boundary condition with cosine base function.
    """
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.cosine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Squared_sine :
    """
    class Custom:

    Describes a boundary condition with squared sine base function.
    """
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.squared_sine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Squared_cosine :
    """
    class Custom:

    Describes a boundary condition with squared cosine base function.
    """
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.squared_cosine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)

