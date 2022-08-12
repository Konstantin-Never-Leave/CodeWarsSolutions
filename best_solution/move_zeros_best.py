def move_zeros(array):
    array.sort(key=lambda v: v == 0)
    return array
