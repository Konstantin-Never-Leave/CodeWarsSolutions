def likes(names):
    likers = 'no one likes this'
    if len(names) == 1:
        likers = f'{names[0]} likes this'
    elif len(names) == 2:
        likers = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        likers = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        likers = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

    return likers
  