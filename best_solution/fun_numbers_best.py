def dig_pow(number, power):
    the_sum = int()
    for index, value in enumerate(str(number)):
        the_sum += pow(int(value), power + index)
    return the_sum / number if the_sum % number == 0 else -1
