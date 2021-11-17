import random
from enum import Enum


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


with open("worte0.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()


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
            if i + y >= height:
                return False
            if grid[y + i][x] != " ":
                return False
        elif direction == WordDirection.horizontal:
            if i + x >= width:
                return False
            if grid[y][x + i] != " ":
                return False
        elif direction == WordDirection.diagonal:
            if i + y >= height or i + x >= width:
                return False
            if grid[y + i][x + i] != " ":
                return False
    return True


def generate_alphabet(difficulty):
    # create alphabet
    if difficulty == Difficulty.hard:
        # TODO: Remove dups and sprinkle in other letters to get to 26 chars
        alphabet = "".join(words).upper()

        while len(alphabet) < 26:
            for i in range(0, 26-len(alphabet)):
                alphabet += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                alphabet_set = set(alphabet)
                alphabet = "".join(alphabet_set)
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet


dimensions = lines[0].split()
height = int(dimensions[0])
width = int(dimensions[1])

difficulty = Difficulty.hard


uncleaned_words = lines[2:]
words = []
# Remove newline chars
for word in uncleaned_words:
    words.append(word.strip())


possible_word_directions = []

if difficulty == Difficulty.easy:
    possible_word_directions = [
        WordDirection.vertical, WordDirection.horizontal]
else:
    possible_word_directions = [WordDirection.vertical,
                                WordDirection.horizontal, WordDirection.diagonal]

# Init grid
grid = [[" "] * width for _ in range(height)]

alphabet = generate_alphabet(difficulty)


# grid = populate_grid(grid, alphabet, width, height, possible_word_directions)

for word in words:
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    direction = random.choice(possible_word_directions)
    reversed = random.choice(
        [True, False]) if difficulty == Difficulty.hard else False
    while not is_word_possible((x, y), word, grid, direction):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        direction = random.choice(possible_word_directions)
    grid = place_word((x, y), word, grid, direction, reversed)

# Fill Grid with random chars
for i in range(0, height):
    for k in range(0, width):
        if grid[i][k] == " ":
            grid[i][k] = alphabet[random.randint(0, 25)]


render(grid)

# print("test")
