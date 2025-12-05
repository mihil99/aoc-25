
FILENAME = "4.input"

grid = []
w = 0
h = 0
with open(FILENAME, 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            w = len(line)
            grid.append([False]*(w+2))
        grid.append(
            [False,
             *list(map(lambda x: True if x == '@' else False, line)),
             False]
        )
    grid.append([False]*(w+2))
    h = len(grid)-2


def check(i, j, _max=3):
    if not grid[i][j]:
        return False
    to_check = [
        grid[i-1][j-1],
        grid[i-1][j],
        grid[i-1][j+1],
        grid[i][j-1],
        grid[i][j+1],
        grid[i+1][j-1],
        grid[i+1][j],
        grid[i+1][j+1]
    ]
    return sum(map(lambda x: 1 if x else 0, to_check)) <= _max


total = 0
for r in range(1, h+1):
    for c in range(1, w+1):
        if check(r, c):
            total += 1

print(f"answer 1: {total}")

total = 0
while True:
    to_remove = []
    for r in range(1, h+1):
        for c in range(1, w+1):
            if check(r, c):
                total += 1
                to_remove.append([r, c])
    if len(to_remove) == 0:
        break
    for r, c in to_remove:
        grid[r][c] = False

print(f"answer 2: {total}")
