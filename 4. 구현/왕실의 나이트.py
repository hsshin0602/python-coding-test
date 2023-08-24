inp = input()

row = int(inp[1])
column = int(ord(inp[0]) - int(ord("a")) + 1)
count = 0
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1
print(count)
