def positive_sum(mixed_array):
    positive_sum = []
    for i in mixed_array:
        if i > 0:
            positive_sum.append(i)
    return sum(positive_sum) if positive_sum else 0
