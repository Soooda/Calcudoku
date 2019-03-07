# Calcudoku
Bored of sudoku? Try calcudoku!

The puzzle is simple. Upon a square n×n grid, each row and column must contain a permutation of the numbers from 1 to n. Consequently, each row or column must contain each of these exactly once.

Overlaid upon the grid are a number of cages. Each cage consists of one or more contiguous cells, and contains a label. A label is a target value V, and optionally an operator, which may be any one of +, −, ∗, /.

A player must place numbers in every cage such that its indicated condition is satisfied. The rule for a given cage depends on its operator:

no operator : the cage must consist of a single square containing V;

∗ : the product of the numbers in the cage must be equal to V;

+ : the sum of the numbers in the cage must be equal to V;

/ : the cage must be exactly two squares, the smaller value of the two must divide the larger one evenly so that the quotient is V;

− : the cage must contain two cells, where the difference of the two members is V.

Your task

Puzzles will be provided in the following way. Here is an example using the picture above.

0 0 1 2 2 3
0 4 4 5 5 3
6 7 8 8 9 9
6 6 10 10 11 11
12 13 13 14 14 15
16 16 13 14 17 15
80* 3 5- 2/ 11+ 1- 9* 2 3- 30* 11+ 2/ 6 8* 13+ 8+ 10* 1
The first six lines describe the cage shapes. All cells assigned the same number share a common cage.

The seventh line contains the cage labels. Which cage a label belongs to depends on its index in the line. So, 80∗ is the condition for cage 0, while 6 is the label upon cage 12. A label will always be a number, followed optionally by an operator symbol.

You should print your solution to standard out, as follows:

5 4 3 1 6 2
4 6 5 2 3 1
3 2 1 4 5 6
1 3 6 5 2 4
6 1 2 3 4 5
2 5 4 6 1 3
Each row must be on a line by itself. Each number is to be separated from the next by a single space.

If a puzzle is unsolvable, you should output No solution.

Notes

All test puzzles will be 6×6.

All test puzzles will have a unique solution, if one exists.

The first six input lines will each consist of exactly six decimal integers separated by spaces.

The cage numbers will be numbered from 0 to m, increasing as new cages are encountered, scanning left to right, top to bottom.

There will be exactly m+1 labels provided on the 7th line, space-separated as above.

Examples

An unsolvable example puzzle:

Input:

0 1 2 2 3 3
4 4 4 5 5 5
4 4 6 6 7 8
9 10 10 11 7 8
9 12 12 13 13 8
14 14 12 13 15 15
6 6 2* 3/ 10+ 6* 6+ 5 24* 2- 2- 2 7+ 20* 8+ 2-
Output:

No solution.
Hints

Consider the use of recursion.

Functions are your friends. Break the problem up into more manageable chunks.

For certain puzzles, direct deduction will only get you so far. At some point you may be forced to make a guess and see if it leads to a violation of the rules.
