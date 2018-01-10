import unittest

from code import split_array


class CodeTestCase(unittest.TestCase):

    def test_should_return_length_4_array_in_0_chunks(self):
        arr = [1, 2, 3, 4]

        res = split_array(arr, 0)

        self.assertEqual([arr], res)


    def test_should_return_length_4_array_in_1_chunks(self):
        arr = [1, 2, 3, 4]

        res = split_array(arr, 1)

        self.assertEqual([arr], res)


    def test_should_return_length_4_array_in_2_chunks(self):
        arr = [1, 2, 3, 4]

        res = split_array(arr, 2)

        self.assertEqual(2, len(res))
        self.assertEqual(
            [
                [1, 2],
                [3, 4],
            ],
            res
        )


    def test_should_return_length_5_array_in_2_chunks(self):
        arr = [1, 2, 3, 4, 5]

        res = split_array(arr, 2)

        self.assertEqual(2, len(res))
        self.assertEqual(
            [
                [1, 2, 3],
                [4, 5],
            ],
            res
        )


    def test_should_return_length_5_array_in_3_chunks(self):
        arr = [1, 2, 3, 4, 5]

        res = split_array(arr, 3)

        self.assertEqual(3, len(res))
        self.assertEqual(
            [
                [1, 2],
                [3, 4],
                [5]
            ],
            res
        )


    def test_should_return_length_5_array_in_4_chunks(self):
        arr = [1, 2, 3, 4, 5]

        res = split_array(arr, 4)

        self.assertEqual(4, len(res))
        self.assertEqual(
            [
                [1],
                [2],
                [3],
                [4, 5]
            ],
            res
        )


    def test_should_return_length_5_array_in_5_chunks(self):
        arr = [1, 2, 3, 4, 5]

        res = split_array(arr, 5)

        self.assertEqual(5, len(res))
        self.assertEqual(
            [
                [1],
                [2],
                [3],
                [4],
                [5]
            ],
            res
        )


    def test_should_return_length_13_array_in_5_chunks(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        res = split_array(arr, 5)

        self.assertEqual(5, len(res))
        self.assertEqual(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13]
            ],
            res
        )


    def test_should_return_length_13_array_in_4_chunks(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        res = split_array(arr, 4)

        self.assertEqual(4, len(res))
        self.assertEqual(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12, 13]
            ],
            res
        )
