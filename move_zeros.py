# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
""" 
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements

example:
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

# --------------------------------------------------->mine solution:<---------------------------------------------------
import unittest


def move_zeros(array):
    for _ in array:
        try:
            array.remove(0)
            array.append(0)
        except ValueError:
            pass

    return array

# --------------------------------------------------->best solution:<---------------------------------------------------


def move_zeros_best(array):
    array.sort(key=lambda v: v == 0)
    return array


# _______________________________________________________TESTS__________________________________________________________


class TestMoveZero(unittest.TestCase):

    def test_move_zero(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([]), [])

    def test_move_zero_best(self):
        self.assertEqual(move_zeros_best(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros_best(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros_best([0, 0]), [0, 0])
        self.assertEqual(move_zeros_best([0]), [0])
        self.assertEqual(move_zeros_best([]), [])


if __name__ == '__main__':
    unittest.main()




# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]