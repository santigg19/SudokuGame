import unittest
from interfaz import Interfaz


class TestInterfazSudoku(unittest.TestCase):


    def test_something_valid(self):

        user = Interfaz()
        result = user.enter(5, 4, 6)
        self.assertTrue(result)

    def test_something_not_valid(self):

        user = Interfaz()
        result = user.enter(11, 4, 6)
        self.assertFalse(result)

    def test_char_in_first_pos(self):

        user = Interfaz()
        result = user.enter("c", 4, 6)
        self.assertFalse(result)

    def test_char_in_second_pos(self):

        user = Interfaz()
        result = user.enter(0, "o", 6)
        self.assertFalse(result)

    def test_char_in_third_pos(self):

        user = Interfaz()
        result = user.enter(0, 4, "d")
        self.assertFalse(result)

    def test_symbol_first(self):

        user = Interfaz()
        result = user.enter("!", 4, 6)
        self.assertFalse(result)

    def test_symbol_second(self):

        user = Interfaz()
        result = user.enter(0, "!", 6)
        self.assertFalse(result)

    def test_symbol_third(self):

        user = Interfaz()
        result = user.enter(0, 4, "!")
        self.assertFalse(result)

    def test_2_symbols(self):

        user = Interfaz()
        result = user.enter("!", 4, "$")
        self.assertFalse(result)

    def test_symbold_and_char(self):

        user = Interfaz()
        result = user.enter("+", "g", 6)
        self.assertFalse(result)

    def test_nothing_valid(self):

        user = Interfaz()
        result = user.enter(".", "%", "d")
        self.assertFalse(result)

    def test_x(self):

        user = Interfaz()
        user.tam = 4
        result = user.enter("x", 1, 1)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()