class Game(object):
    """Classic two-player board game whereby a player can win by getting
    a certain number of their pieces on the board in a row. Default version
    is Connect Four."""

    def __init__(self, rows=6, columns=7, win_length=4):
        """Defaults to standard board size of 7 across, 6 deep.

        Default win-length is 4, i.e. this is "Connect Four"."""

        self._board = [[0 for i in xrange(columns)] for i in xrange(rows)]
        self._rows = rows
        self._columns = columns
        self._win_length = win_length
        self.current_player = None
        self.winner = None
        print "The game is afoot!"

    @staticmethod
    def _players():
        """Generator for players."""
        while True:
            yield 1
            yield 2

    def render_board(self):
        """Displays the current state of the game board."""
        print ""
        for row in self._board:
            print row

    def update(self, move):
        """Adds the current move to the board, raises an InvalidMove exception
        if the move is not valid.

        Move is provided as a number representing the column (0-indexed)."""

        if not 0 <= move < 7:
            raise InvalidMove

        placed = False
        x = None
        y = None

        for row in reversed(xrange(self._rows)):
            if not self._board[row][move]:
                self._board[row][move] = self.current_player
                placed = True
                x = move
                y = row
                break

        if not placed:
            raise InvalidMove

        return (x, y)

    def evaluate_board(self, x, y):
        """Evaluates the current board to see if a win or draw has occured."""

        if self.won(x, y) or self.draw():
            raise GameOver("The game has ended.")

    def won(self, x, y):
        """Returns boolean for whether or not the current player has won."""

        segments = [self.get_horizontal(x, y),
                    self.get_vertical(x, y),
                    self.get_diagonal_up(x, y),
                    self.get_diagonal_down(x, y)]

        for segment in segments:
            if self.match(segment):
                self.winner = self.current_player
                print "Congratulations, Player {} has won!".format(self.current_player)
                return True

        return False

    def get_horizontal(self, x, y):
        """A horizontal segment.

        Returns the values from the row containing the given position."""

        return self._board[y]

    def get_vertical(self, x, y):
        """A vertical segment.

        Returns the values from the column containing the given position."""

        return [row[x] for row in self._board]

    def get_diagonal_up(self, x, y):
        """A diagonal segment, upwards from left to right.

        Returns the values from that diagonal (going upward to the right)
        containing the given position."""

        while 0 <= x < 7 and 0 <= y < 6:
            x -= 1
            y += 1

        return [self._board[y-i][x+i] for i in xrange(7)
                if 0 <= (x+i) < 7 and 0 <= (y-i) < 6]

    def get_diagonal_down(self, x, y):
        """A diagonal segment, downwards from left to right.

        Returns the values from that diagonal (going downward to the right)
        containing the given position."""

        while 0 <= x < 7 and 0 <= y < 6:
            x -= 1
            y -= 1

        return [self._board[y+i][x+i] for i in xrange(7)
                if 0 <= (x+i) < 7 and 0 <= (y+i) < 6]

    def match(self, segment):
        """Creates subsegments and sees if any of them are a winning match."""

        match_len = self._win_length

        subsegments = [[segment[j+i] for i in range(match_len)] for j in range(len(segment)-match_len+1)]

        for subsegment in subsegments:
            if set(subsegment).pop() == self.current_player and len(list(set(subsegment))) == 1:
                return True

        return False

    def draw(self):
        """Returns boolean for whether or not the board is filled."""

        for row in self._board:
            for slot in row:
                if slot == 0:
                    return False
        print "It's a draw!"
        return True

    def turn(self, player):
        "Flow of each player's turn within the game."

        self.current_player = player
        print "current_player:", self.current_player
        while True:
            move = int(raw_input("\nHey player {}, what's your move?\n> ".format(player)))
            try:
                x, y = self.update(move)
                break
            except InvalidMove:
                print "Sorry, that move is not valid. Try again!"

        game.render_board()
        game.evaluate_board(x, y)


class InvalidMove(Exception):
    """Exception that gets raised when a move is not valid.

    Raised in the following cases:
    - if a player tries to place a game piece into a completely filled column
    - if a player tries to place a game piece in a non-existent column"""


class GameOver(Exception):
    """Exception that gets raised when the game has ended.

    GameOver scenarios include one player winning, or the game ending in a
    draw (board completely filled, with neither player having won)."""


if __name__ == "__main__":
    game = Game()
    game.render_board()
    for player in game._players():
        try:
            game.turn(player)
        except GameOver:
            break
