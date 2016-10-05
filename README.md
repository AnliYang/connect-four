# connect-four
___

Simple command line interface implementation of the classic game of
[Connect Four](https://en.wikipedia.org/wiki/Connect_Four).

Two players take turns, and indicate their desired move by specifying
the 0-indexed column in which they wish to place their piece. (The
options for valid move columns are 0-6, inclusive.)

Here's what an empty board looks like:
```
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
```

A winning combination of four-in-a-row can be achieved horizontally,
vertically, or diagonally.
