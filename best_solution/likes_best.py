LIKES = {
        0: 'no one likes this',
        1: '%s likes this',
        2: '%s and %s like this',
        3: '%s, %s and %s like this',
        4: '%s, %s and %s others like this'
    }


def likes_best(names):
    if len(names) > 3:
        return LIKES[4] % (names[0], names[1], len(names) - 2)
    return LIKES[len(names)] % tuple(names)
  