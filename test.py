import unittest
import tictac


class TestTT(unittest.TestCase):
    def setUp(self):
        print("set")

    def tearDown(self):
        print("tearD")

    def testCheck_Win(self):
        board1 = ('X', 'X', 'X', 'O', 'X', 'O')
        self.assertEqual(tictac.check_win(board1), 'X')

    def testCheck_Fail(self):
        board2 = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O')
        self.assertEqual(tictac.check_win(board2), False)

    def testCheck_input_incorrect(self):
        self.assertEqual(tictac.start('p'), False)

    def testCheck_input_forX(self):
        self.assertEqual(tictac.start('x'), 'X')

    def testCheck_input_forO(self):
        self.assertEqual(tictac.start('0'), 'O')


if __name__ == '__main__':
    unittest.main()
