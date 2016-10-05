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

        if (self.win_horizontal(x, y)
            or self.win_vertical(x, y)
            or self.win_diagonal_down(x, y)
            or self.win_diagonal_up(x, y)):
            self.winner = self.current_player
            print "Congratulations, Player {} has won!".format(self.current_player)
            return True

        return False

    def win_horizontal(self, x, y):
        """A horizontal win."""

        segment = self._board[y]

        if self.match(segment):
            return True

        return False

    def win_vertical(self, x, y):
        """A vertical win."""

        segment = [row[x] for row in self._board]

        if self.match(segment):
            return True

        return False

    def win_diagonal_up(self, x, y):
        """A diagonal win, upwards from left to right."""

        while 0 <= x < 7 and 0 <= y < 6:
            x -= 1
            y += 1

        segment = [self._board[y-i][x+i] for i in xrange(7)
                   if 0 <= (x+i) < 7 and 0 <= (y-i) < 6]

        if self.match(segment):
            return True

        return False

    def win_diagonal_down(self, x, y):
        """A diagonal win, downwards from left to right."""

        while 0 <= x < 7 and 0 <= y < 6:
            x -= 1
            y -= 1

        segment = [self._board[y+i][x+i] for i in xrange(7)
                   if 0 <= (x+i) < 7 and 0 <= (y+i) < 6]

        if self.match(segment):
            return True

        return False

    def match(self, segment):
        """Creates subsegments and sees if any of them are a winning match."""

        match_len = self._win_length

        subsegments = [[segment[j+i] for i in range(match_len)] for j in range(len(segment)-match_len+1)]
        # from pprint import pprint
        # pprint(subsegments)

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
            # get their move
            # update the board
            # show the new board
            # decide if it's game over or not
        self.current_player = player
        print "current_player:", self.current_player
        while True:
            move = int(raw_input("\nHey player {}, what's your move?\n> ".format(player)))
            try:
                x, y = self.update(move)
                # print "x:", x
                # print "y:", y
                break
            except InvalidMove:
                print "Sorry, that move is not valid. Try again!"

        game.render_board()
        game.evaluate_board(x, y)


class InvalidMove(Exception):
    """Exception that gets raised when a move is not valid.

    If a player tries to place a game piece into a completely filled column,
    the move will come back as invalid."""


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
