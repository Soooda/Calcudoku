'''
Definations
'''
# baseNumber stores the range of number that can put in the grid
baseNumber = list(range(1,7))

# historyPoint list stores the coordinates of points that have been went through
historyPoint = []

# repeatDict stores the coordinates as keys and the possible values being went through as values
repeatDict = {}

# pringResult() takes a 2-D list and print it in the given format
def printResult(answer):
	for line in answer:
		i = 0
		while i < len(line) - 1:
			print(line[i],end=' ')
			i += 1
		print(line[len(line) - 1])
	return

# hasOnlyNumber() checks the given string whether it consists of numbers only
def hasOnlyNumber(inputString):
	for char in inputString:
		if not char.isdigit():
			return False
	return True

# removeRepeatNumber(x,y) returns a list of number that particular point can put in
def removeRepeatNumber(x,y):
    result = baseNumber.copy()
    
    waitRemoveNumber = []

    # Remove numbers based on corresponding cages
    index = grid[x][y]
    op = ops[index][-1]
    value = int(ops[index][:len(ops[index]) - 1])
    # Count how many blocks are in the cage
    count = 0
    for line in grid:
        for n in line:
            if n == index:
                count += 1
    
    # Auto fill
    values = []
    for r in range(6):
        for c in range(6):
            # Exclude itself
            if r == x and c == y:
                continue
            elif grid[r][c] == index:
                values.append(answer[r][c])
    if 0 not in values:
        if op == '+':
            number = value - sum(values)
            if number not in baseNumber:
                return []
            else:
                waitRemoveNumber = baseNumber.copy()
                waitRemoveNumber.remove(number)
        elif op == '*':
            product = 1
            for n in values:
                product *= n
            
            if (value // product) in baseNumber and value % product == 0:
                waitRemoveNumber = baseNumber.copy()
                waitRemoveNumber.remove(value // product)
            else:
                return []
        elif op == '-':
            if value != 0:
                number = values[0]
                if (number + value) not in baseNumber and (number - value) not in baseNumber:
                    return []
                else:
                    waitRemoveNumber = baseNumber.copy()
                    if (number + value) in baseNumber:
                        waitRemoveNumber.remove(number + value)
                    if (number - value) in baseNumber:
                        waitRemoveNumber.remove(number - value)
            else:
                values.sort()
                values.reverse()
                number = values[0]
                for i in range(1,len(values)):
                    number -= values[i]
                if number in baseNumber:
                    waitRemoveNumber = baseNumber.copy()
                    waitRemoveNumber.remove(number)
                else:
                    return []
        elif op == '/':
            number = values[0]
            if(number * value) not in baseNumber and (number // value) not in baseNumber and number % value == 0:
                return []
            else:
                waitRemoveNumber = baseNumber.copy()
                if (number * value) in baseNumber:
                    waitRemoveNumber.remove(number * value)
                if (number // value) in baseNumber and number % value == 0:
                    waitRemoveNumber.remove(number // value)

            
    # Remove numbers that appears in the line and column
    for i in range(6):
        if answer[i][y] != 0 and answer[i][y] not in waitRemoveNumber:
            waitRemoveNumber.append(answer[i][y])
        if answer[x][i] != 0 and answer[x][i] not in waitRemoveNumber:
            waitRemoveNumber.append(answer[x][i])

    # Remove all the numbers found so far
    for n in waitRemoveNumber:
        result.remove(n)
    
    # Remove numbers that have been tried so far
    if (x,y) in repeatDict:
        removeList = repeatDict.get((x,y))
        for n in removeList:
            if n in result:
                result.remove(n)
    
    return result

'''
INPUT
'''
# "grid" is a list that stores the cage shapes
grid = []

# Store the input lines into variable
for i in range(6):
	temp = input().split()
	temp = [int(line) for line in temp] 
	grid.append(temp)

# "answer" is a list that stores the answer grid
answer = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

# "ops" is a list that stores the operators
ops = input().split()

'''
Format Detection Process
'''
# Each line in grid should be length of 6
for line in grid:
	if len(line) != 6:
		print("No solution.")
		exit()

# There will be exactly m+1 labels provided on the 7th line, space-separated as above.
# Find the maximum of numbers in "grid"
temp = 0
for r in range(6):
    for c in range(6):
        if grid[r][c] > temp:
            temp = grid[r][c]
if len(ops) != temp + 1:
	print("No solution.")
	exit()

# String segments that have numbers only but the index appear multiple times in the grid
# Go through each op in ops
i = 0
while i < len(ops):
	# Find string segments with numbers only
	if hasOnlyNumber(ops[i]):
		# Set a temporary variable to store how many times the index repeats
		count = 0
		for line in grid:
			if i in line:
				count += line.count(i)
		
		# If the index repeats, no solution available
		if count > 1:
			print("No solution.")
			exit()
	
	# Increment
	i += 1

'''
Process
'''
# Deal with criteria that don't have any operators
i = 0
# Go through each op in ops
while i < len(ops):
	# Find string segments with numbers only
	if hasOnlyNumber(ops[i]):
		# Identify the block based on the index
		r = 0
		while r < len(grid):
			c = 0
			while c < len(grid[r]):
				if grid[r][c] == i:
					answer[r][c] = int(ops[i])
				c += 1
			r += 1
	i += 1

# Initial the cooridnate and flag
x = 0
y = 0
flag = True

while flag:
    # When block has a zero
    if (answer[x][y] == 0):
        key = (x,y)
        waitNumber = removeRepeatNumber(x,y)

        # Fill in
        if (len(waitNumber) != 0):
            historyPoint.append(key)
            # Get the values that this block has already tried
            if key not in repeatDict:
                repeatDict[key] = []
            answer[x][y] = waitNumber[0]
            repeatDict.get(key).append(waitNumber[0])

        # When go in to a dead end, step back
        elif(len(historyPoint) != 0):
            if key in repeatDict:
                repeatList = repeatDict.get(key)
                if(len(repeatList) != 0):
                    repeatList.clear()
            history = historyPoint[-1]
            x = history[0]
            y = history[1]
            historyPoint.remove(history)
            answer[x][y] = 0
            continue
        # Unsolvable
        else:
            print("No solution.")
            exit()
    # Loop through each row and line
    y += 1
    if y >= 6:
        y = 0
        x += 1

    # Condition when the loop stops
    if x >= 6:
        flag = False
            
'''
Output Formation
'''
# Check if numbers repeat
for line in answer:
    for n in range(1,7):
        if line.count(n) != 1:
            print('No solution.')
            exit()

printResult(answer)
