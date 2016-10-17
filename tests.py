import unittest
from connect_four_oo import Game

"""Some thoughts:
unit tests: for each functions (that don't require a pre-existing state)

integration tests: testing the API, so instantiating a game, setting up a board,
    and feeding in an update to see if it updates the board corectly

functional tests: need to move making moves (taking turns), to play a game
- mocking raw input

* DONE does _players, given a limit, output correctly?
* DONE given a brand-new game,
    * DONE does render_board() output empty board correctly?
    * DONE do the default values for rows, columns, and win_length work?
    * DONE does it work to pass in rows, columns, and win_length?
* given a board and move, does update():
    * return the predicted/correct value?
    * raise InvalidMove exception when necessary?
    * change the state of the board correctly?
* given a board and position, does the GameOver exception get raised correctly?
    * case of non-win with non-full board
    * case of draw
    * case for each type of win (horizontal, vertical, 2 diagonals)
    * different cases by player?
* given a board and position, can you get the predicted
    * vertical segment?
    * horizontal segment?
    * diagonal-up segment?
    * diagonal_down segment?
* given a segment, is match correctly predicted?
    * case for each type of segment?
* given a board, is it a draw?
    * case when not a draw and case when is
* for a given player and turn:
    * does the game's current_player attribute get updated correctly?
    * given a particular move,
        * does the position returned by update match prediction?
        * does the board get updated correctly (check _board value)?
    * is render_board() called within each turn?
    * is evalute_board() called within each turn?
* given a game log, does the right result (draw, win+player combo) occur?
"""

class ConnectFourUnitTest(unittest.TestCase):
    """Unit tests for Connect Four."""

    def test_players(self):
        players = Game._players()

        self.assertEqual(players.next(), 1)
        self.assertEqual(players.next(), 2)
        self.assertEqual(players.next(), 1)

    def test_board(self):
        game = Game()
        empty_board = [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(game._board, empty_board)

    def test_rows_default(self):
        game = Game()
        self.assertEqual(game._rows, 6)

    def test_columns_default(self):
        game = Game()
        self.assertEqual(game._columns, 7)

    def test_win_length_default(self):
        game = Game()
        self.assertEqual(game._win_length, 4)

    def test_rows_non_default(self):
        game = Game(rows=3)
        self.assertEqual(game._rows, 3)

    def test_columns_non_default(self):
        game = Game(columns=3)
        self.assertEqual(game._columns, 3)

    def test_win_length_non_default(self):
        game = Game(win_length=3)
        self.assertEqual(game._win_length, 3)

    def test_current_player(self):
        game = Game()
        self.assertIsNone(game.current_player)

    def test_winner(self):
        game = Game()
        self.assertIsNone(game.winner)

    def test_render_board(self):
        game = Game()

        with captured_output() as out:
            game.render_board()

        rendered_empty_board = """[0, 0, 0, 0, 0, 0, 0]
                                  [0, 0, 0, 0, 0, 0, 0]
                                  [0, 0, 0, 0, 0, 0, 0]
                                  [0, 0, 0, 0, 0, 0, 0]
                                  [0, 0, 0, 0, 0, 0, 0]
                                  [0, 0, 0, 0, 0, 0, 0]"""

        self.assertBoardEqual(out.getvalue().strip(), rendered_empty_board)

    def assertBoardEqual(self, board1, board2):
        """Compare boards for matchingness, disregarding whitespace,
        which the computer cares about but humans do not in this case."""
        # other assert functions that do things the way I want them to do
        # raises AssertionError or nothing
        self.assertEqual(board1.split(), board2.split())


#### HELPER FUNCTIONS
# Context Manager for getting printed output into an object
from contextlib import contextmanager
from StringIO import StringIO
import sys

@contextmanager
def captured_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


if __name__ == "__main__":
    unittest.main()
