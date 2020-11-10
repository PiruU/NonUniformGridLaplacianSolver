import check as chk
import boundary_condition_functions as function

class Custom :
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
        return self._function(coordinate, self._params) if chk.is_in_unit_segment(coordinate) else 0.0


class Constant :
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.constant).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Sine :
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.sine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Cosine :
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.cosine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Squared_sine :
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.squared_sine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)


class Squared_cosine :
    def __init__(self) :
        self._boundary_condition = Custom().set_function(function.squared_cosine).set_params(function.default_params)

    def set_amplitude(self, amplitude) :
        self._boundary_condition.set_params({'amplitude' : amplitude  })
        return self

    def value(self, coordinate) :
        return self._boundary_condition.value(coordinate)

