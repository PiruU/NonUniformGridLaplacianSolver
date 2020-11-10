import default
import types

def make() :
    """
    Returns a manager with all four zero-constant boundary conditions
    """
    return Handle()


class Handle :
    """
    Class Handler:

    This class is designed to handle exactly 4 boundary conditions.
    Boundary consitions are designated to be on north-south-east or west direction.
    This positioning system is related to the Ouv coordinates system.
    """
    def __init__(self) :
        self._conditions = [types.make_constant()] * default.n_conditions

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

