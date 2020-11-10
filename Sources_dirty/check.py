import default


def has_two_coordinates(container) :
    return len(container) == default.n_dimensions


def is_valid_axis_index(i_direction) :
    return i_direction == default.index_u or i_direction == default.index_v


def is_in_unit_segment(coordinate) :
    return coordinate >= 0 and coordinate <= 1

