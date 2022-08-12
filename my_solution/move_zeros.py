def move_zeros(array):
    for _ in array:
        try:
            array.remove(0)
            array.append(0)
        except ValueError:
            pass

    return array
