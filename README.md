# Calcudoku
这个题目来自我大一上学期编程Online Challenges，我认为是我那个学期经历的最棘手的问题（没有之一）QwQ

**本篇文章仅包含题目的内容，感兴趣的朋友一起讨论交流，我会在之后的文章里分享我的思路和代码～**

首先是原汁原味的**英文**:

------

カルクドク
------------------------------
![Calcudoku](https://img-blog.csdnimg.cn/20190205001837388.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvZGFhYWFh,size_16,color_FFFFFF,t_70)

Bored of sudoku? Try calcudoku!

The puzzle is simple. Upon a square n×n grid, each row and column must contain a permutation of the numbers from 1 to n. Consequently, each row or column must contain each of these ==exactly once==.

Overlaid upon the grid are a number of cages. Each cage consists of one or more contiguous cells, and contains a label. A label is a target value V, and optionally an operator, which may be any one of +, −, ∗, /.

A player must place numbers in every cage such that its indicated condition is satisfied. The rule for a given cage depends on its operator:
- **no operator** : the cage must consist of a single square containing V;
- ∗ : the product of the numbers in the cage must be equal to V;
- \+ : the sum of the numbers in the cage must be equal to V;
- / : the cage must be exactly two squares, the smaller value of the two must divide the larger one evenly so that the quotient is V;
- − : the cage must contain two cells, where the difference of the two members is V.

**Your task**
Puzzles will be provided in the following way. Here is an example using the picture above.
```
0 0 1 2 2 3
0 4 4 5 5 3
6 7 8 8 9 9
6 6 10 10 11 11
12 13 13 14 14 15
16 16 13 14 17 15
80* 3 5- 2/ 11+ 1- 9* 2 3- 30* 11+ 2/ 6 8* 13+ 8+ 10* 1
```
The first six lines describe the cage shapes. All cells assigned the same number share a common cage.

The seventh line contains the cage labels. Which cage a label belongs to depends on its index in the line. So, 80∗ is the condition for cage 0, while 6 is the label upon cage 12. A label will always be a number, followed optionally by an operator symbol.

You should print your solution to standard output, as follows:
```
5 4 3 1 6 2
4 6 5 2 3 1
3 2 1 4 5 6
1 3 6 5 2 4
6 1 2 3 4 5
2 5 4 6 1 3
```
Each row must be on a line by itself. Each number is to be separated from the next by a single space.

If a puzzle is unsolvable, you should output ==No solution.==

**Notes**
- All test puzzles will be 6×6.

- All test puzzles will have a unique solution, if one exists.

- The first six input lines will each consist of exactly six - -decimal integers separated by spaces.

- The cage numbers will be numbered from 0 to m, increasing as new cages are encountered, scanning left to right, top to bottom.

- There will be exactly m+1 labels provided on the 7th line, space-separated as above.

**Examples**
An unsolvable example puzzle:

Input:
```
0 1 2 2 3 3
4 4 4 5 5 5
4 4 6 6 7 8
9 10 10 11 7 8
9 12 12 13 13 8
14 14 12 13 15 15
6 6 2* 3/ 10+ 6* 6+ 5 24* 2- 2- 2 7+ 20* 8+ 2-
```

Output:
```
No solution.
```

**Hints**
- Consider the use of recursion.

- Functions are your friends. Break the problem up into more manageable chunks.

- For certain puzzles, direct deduction will only get you so far. At some point you may be forced to make a guess and see if it leads to a violation of the rules.

----
本人中文翻译：

算术数独
--
![算术数独](https://img-blog.csdnimg.cn/20190205001913533.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvZGFhYWFh,size_16,color_FFFFFF,t_70)
写程序解一般数独太轻松？来试试算术数独吧！

规则非常简单，在n x n尺寸的表格中各行各列都填入数字1 ～ n，同时保证每行每列都**没有重复**的数字。

整个表格被粗线分成若干个框框，而每个框框都包含至少一个格子以及一个标签。一个标签又由一个目标值和一个运算符（==当框框里只含有一个格子时，不需要运算符==）组成。

玩家在把数字填入格子中时要使框框的要求满足。而具体的要求，由标签中的运算符决定：
- **没有运算符**：这个框框一定只有一个格子，同时格子里填的数一定是标签上的目标值。
- *：框框中各个格子的数字的乘积等于目标值。
- +：框框中各个格子的数字的和等于目标值。
- /：框框中有且只包含两个格子，同时较大的数字能整除较小的数字所得的商等于目标值。
- -：框框中有且只包含两个格子，同时两数的差等于目标值。

**你需要做的工作**
具体的数独表格会按以下格式输入。以下代码是以图片中的题目为例输入的:
```
0 0 1 2 2 3
0 4 4 5 5 3
6 7 8 8 9 9
6 6 10 10 11 11
12 13 13 14 14 15
16 16 13 14 17 15
80* 3 5- 2/ 11+ 1- 9* 2 3- 30* 11+ 2/ 6 8* 13+ 8+ 10* 1
```
前六行的数字，描述了题目中各个框框的具体形状。数字相同的格子代表它们在同一个框框中。
第七行按顺序则相继代表各个框框所对应的标签。比如 80*是0号框框所对应的标签，6 则对于数字12所在的框框。标签的输入格式永远是目标值在前，运算符在后（需要运算符的情况下）。

你需要将求出的答案，按以下格式print出来。
```
5 4 3 1 6 2
4 6 5 2 3 1
3 2 1 4 5 6
1 3 6 5 2 4
6 1 2 3 4 5
2 5 4 6 1 3
```
行对行列对列，数字之间以空格隔开。
如果所给题目无解，需要print **No solution.**

**注意事项（本栏下的内容主要是说明我们挑战审核系统里面testcases的一些细节，可忽略）**
- 所有testcases的尺寸都是6 x 6。
- 所有testcases在有解的前提下，都有唯一解。
- 所有testcases 前6行的input都是范围内的整数，并以空格隔开。
- 前六行的input框框标号都是从0开始到m，顺序从左到右从上到下。
- 第七行共有m + 1个标签输入，相互以空格隔开。

**例子**
一个无解的例题
输入：
```
0 1 2 2 3 3
4 4 4 5 5 5
4 4 6 6 7 8
9 10 10 11 7 8
9 12 12 13 13 8
14 14 12 13 15 15
6 6 2* 3/ 10+ 6* 6+ 5 24* 2- 2- 2 7+ 20* 8+ 2-
```

输出：
```
No solution.
```
**提示（学校好良心QwQ）**
- 考虑用用递归。
- 自己def函数是一个好办法，尽量把一个复杂的问题拆分成数个部分解决。
- 对于一些情况，直接推导并不能走的太远。有时你可能需要通过猜来推进，再观察结果是否违背了要求。

