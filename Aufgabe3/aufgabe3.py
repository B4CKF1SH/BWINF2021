import random
from enum import Enum


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def reversed_string(a_string):
    return a_string[::-1]


def render(grid):
    for row in range(height):
        print(" ".join(grid[row]))


class Difficulty(Enum):
    easy = 1
    medium = 2
    hard = 3


class WordDirection(Enum):
    vertical = 1
    horizontal = 2
    diagonal = 3


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
height = 10
width = 10
possible_word_directions = [WordDirection.vertical,
                            WordDirection.horizontal, WordDirection.diagonal]

# Init grid
grid = [[" "] * width for _ in range(height)]


# Place Words


def place_word(pos, word, grid, direction, reversed):
    x, y = pos
    space = len(word)
    # TODO: Place words backwards and diagonally
    for i in range(space):
        if direction == WordDirection.vertical:
            grid[y + i][x] = reversed_string(word)[i] if reversed else word[i]
        elif direction == WordDirection.horizontal:
            grid[y][x + i] = reversed_string(word)[i] if reversed else word[i]
        elif direction == WordDirection.diagonal:
            grid[y + i][x +
                        i] = reversed_string(word)[i] if reversed else word[i]
    return grid


def is_word_possible(pos, word, grid, direction):
    x, y = pos
    space = len(word)
    for i in range(space):
        if direction == WordDirection.vertical:
            if i + y >= width:
                return False
            if grid[y + i][x] != " ":
                return False
        elif direction == WordDirection.horizontal:
            if i + x >= height:
                return False
            if grid[y][x + i] != " ":
                return False
        elif direction == WordDirection.diagonal:
            if i + y >= width or i + x >= height:
                return False
            if grid[y + i][x + i] != " ":
                return False
    return True


words = ["test", "dogs", "cats"]
for word in words:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    direction = random.choice(possible_word_directions)
    reversed = random.choice([True, False])
    while not is_word_possible((x, y), word, grid, direction):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    grid = place_word((x, y), word, grid, direction, reversed)


# print(render(place_word((1, 1), "test", grid)))
#print(is_word_possible((1, 9), "test", grid, True))
# Fill Grid with random chars
for i in range(0, width):
    for k in range(0, height):
        if grid[i][k] == " ":
            grid[i][k] = alphabet[clamp(
                int(random.randint(0, 25) * 1.1), 0, 25)]  # TODO:  needs work for different difficulties


render(grid)

# print("test")
