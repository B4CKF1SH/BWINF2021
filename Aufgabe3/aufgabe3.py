import random


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def render(grid):
    for row in range(height):
        print(" ".join(grid[row]))


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
height = 10
width = 10

# Init grid
grid = [[" "] * width for _ in range(height)]


# Place Words
vertical = random.choice([True, False])


def place_word(pos, word, grid, vertical):
    x, y = pos
    space = len(word)
    for i in range(space):
        if vertical:
            grid[y + i][x] = word[i]
        else:
            grid[y][x + i] = word[i]
    return grid


def is_word_possible(pos, word, grid, vertical):
    x, y = pos
    space = len(word)
    for i in range(space):
        if vertical:
            if i + y >= width:
                return False
            if grid[y + i][x] != " ":
                return False
        else:
            if i + x >= height:
                return False
            if grid[y][x + i] != " ":
                return False
    return True


words = ["test"]
for word in words:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    while not is_word_possible((x, y), word, grid, vertical):
        # print("ITER")
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    grid = place_word((x, y), word, grid, vertical)


# print(render(place_word((1, 1), "test", grid)))
#print(is_word_possible((1, 9), "test", grid, True))
# Fill Grid with random chars
for i in range(0, width):
    for k in range(0, height):
        if grid[i][k] == " ":
            grid[i][k] = alphabet[clamp(
                int(random.randint(0, 25) * 1.1), 0, 25)]


render(grid)

print("test")
