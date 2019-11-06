import unittest

from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_same_number_in_a_row(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "3", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.insert_number(3, 1, 8, 0))

    def test_same_number_in_a_column(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.validar(3, 8, 2))

    def test_same_number_in_a_box(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "3", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.validar(3, 2, 3))

    def test_something_valid(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        sudoku.insert_number(1, 1, 3, 0)
        self.assertFalse(sudoku.insert_number(1, 1, 3, 0))

    def test_different_values(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        sudoku.insert_number(1, 0, 2, 0)

        sudoku.insert_number(1, 1, 2, 0)

        self.assertNotEqual(sudoku.board[0][0], sudoku.board[1][2])

    def test_insert_a_valid_number(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        sudoku.insert_number(2, 0, 2, 0)
        self.assertTrue(sudoku.insert_number)


    def test_if_win_false(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["x", "x", "x", "2", "x", "x", "x", "6", "x"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.winner())

    def test_if_win_true(self):

        sudoku = Sudoku([["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])

        self.assertTrue(sudoku.winner())


    def test_insert_a_number_in_a_non_valid_position(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])


        self.assertFalse(sudoku.insert_number(2, 8, 8, 0))

    def test_Sudoku_6(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])


        self.assertFalse(sudoku.insert_number(2, 0, 2, 0))
    
    def test_non_valid(self):
        
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])

        self.assertFalse(sudoku.insert_number(0, 3, 1, 0))
    
    def test_not_valid_move(self):

        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])

        self.assertFalse(sudoku.insert_number(1, 3, 3, 0))
    
    def test_bad_choice(self):

        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])

        self.assertFalse(sudoku.insert_number(3, 1, 3, 0))

    def test_Sudoku_Valor_Fijo_ch(self):

        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])

        self.assertFalse(sudoku.insert_number(1, 3, 2, 0))
    
    def test_win_4(self):

        sudoku = Sudoku([["4", "3", "2", "1"],
                         ["2", "1", "3", "4"],
                         ["3", "4", "1", "2"],
                         ["1", "2", "4", "3"]])

        self.assertTrue(sudoku.winner())

    def test_not_win_4(self):

        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])

        self.assertFalse(sudoku.winner())




if __name__ == '__main__':
    unittest.main()