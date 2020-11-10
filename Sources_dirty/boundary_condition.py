import default
import boundary_condition_types as types

def make_constant(amplitude = 0) :
    return types.Constant().set_amplitude(amplitude)


def make_squared_sine(amplitude = 1) :
    return types.Squared_sine().set_amplitude(amplitude)


def make_squared_cosine(amplitude = 1) :
    return types.Squared_cosine().set_amplitude(amplitude)


def make_sine(amplitude = 1) :
    return types.Sine().set_amplitude(amplitude)


def make_cosine(amplitude = 1) :
    return types.Cosine().set_amplitude(amplitude)


class Manager :
    def __init__(self) :
        self._conditions = [default.condition_type] * default.n_conditions

    def set_north_condition(self, condition) :
        return self.set_condition(default.index_north, condition)

    def set_south_condition(self, condition) :
        return self.set_condition(default.index_south, condition)

    def set_west_condition(self, condition) :
        return self.set_condition(default.index_west, condition)

    def set_east_condition(self, condition) :
        return self.set_condition(default.index_east, condition)

    def set_condition(self, i_condition, condition) :
        self._conditions[i_condition] = condition
        return self

    def get_condition(self, i_condition) :
        return self._conditions[i_condition]

