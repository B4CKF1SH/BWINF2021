import random
from enum import Enum


def reversed_string(s):
    """Gibt einen String in umgekehrter Reihenfolge zurück."""
    return s[::-1]


def render(grid, words):
    """Gibt ein Gitter in die Konsole, so wie die gesuchten Wörter.

    Argumente:
    grid -- Auszugebene Gitter
    words -- Gesuchte Wörter

    Rückgabe:
    None
    """
    for row in range(height):
        print(" ".join(grid[row]))
    print("-" * 20)
    print("Gesuchte Wörter:")
    for word in words:
        print(word.capitalize())
    print("\n")


class Difficulty(Enum):
    """Mögliche Schwierigkeitsstufen"""
    easy = 1
    medium = 2
    hard = 3


class WordDirection(Enum):
    """Ausrichtung eines Wortes im Gitter"""
    vertical = 1
    horizontal = 2
    diagonal = 3


def place_word(pos, word, grid, direction, reversed):
    """Platziert ein Wort an gegebener Position.

    Argumente:
    pos -- Tupil mit x und y Koordinaten des Wortes
    word -- Das zu platzierende Wort als String
    grid -- Das Gitter in dem das Wort platziert werden soll
    direction -- Ausrichtung des Wortes im Gitter 
    reversed -- Gibt an ob das Wort rückwärts eingefügt werden soll 

    Rückgabe:
    grid -- Das neue Gitter mit dem neu eingefügten Wort
    """
    x, y = pos
    space = len(word)
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
    """Überprüft, ob es möglich ist, ein Wort an gegebener Position einzufügen.

    Argumente:
    pos -- Tupil mit x und y Koordinaten des Wortes
    word -- Das zu überprüfende Wort als String
    grid -- Das Gitter in dem das Wort platziert werden soll
    direction -- Ausrichtung des Wortes im Gitter 

    Rückgabe:
    True || False -- Das Wort kann (nicht) eingefügt werden
    """
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


def generate_alphabet(difficulty, words):
    """Erstellt eine Zeichenkette mit 26 Zeichen, basierend auf der Schwierigkeitsstufe.

    Argumente:
    difficulty -- Schwierigkeitsstufe
    words -- Wörtern aus denen ein Alphabet generiert wird

    Rückgabe:
    alphabet -- String mit 26 Zeichen
    """
    # create alphabet
    if difficulty == Difficulty.hard:
        # Erstellen des Alphabets aus Buchstaben der gesuchten Wörter
        alphabet = "".join(words).upper()

        # Auffüllen des Alphabets mit zufälligen Buchstaben
        while len(alphabet) < 26:
            for _ in range(0, 26-len(alphabet)):
                alphabet += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                # Löschen von Duplikaten aus dem Array durch Konvertierung in ein Set
                alphabet_set = set(alphabet)
                alphabet = "".join(alphabet_set)
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet


def populate_grid(in_grid, alphabet, difficulty, width, height, words, possible_word_directions):
    """Füllt das Gitter mit Wörtern und leere Stellen mit Buchstaben aus dem generierten Alphabet auf.

    Argumente:
    in_grid -- Das Gitter, das gefüllt werden soll
    alphabet -- In `generate_alphabet()` generierte Zeichenkette
    difficulty -- Gewollte  Schwierigkeitsstufe des Gitters
    width -- Breite des Gitters 
    height -- Höhe des Gitters 
    words -- Liste mit einzufügenden Wörtern 
    possible_word_directions -- Mögliche Ausrichtungen eines Wortes 

    Rückgabe:
    grid -- Das aufgefüllte Gitter
    """

    grid = in_grid
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

    # Füllen des Gitters mit zufälligen Buchstaben des generierten Alphabets
    for i in range(0, height):
        for k in range(0, width):
            if grid[i][k] == " ":
                grid[i][k] = alphabet[random.randint(0, 25)]

    return grid


def create_game(difficulty, words, width, height):
    """Generiert alle benötigten Werte, um ein neues Gitter zu erstellen.

    Argumente:
    difficulty -- Schwierigkeitsstufe
    words -- Wörter die im Puzzle gesucht werden sollen
    width -- Breite des Gitters
    height -- Höhe des Gitters

    Rückgabe:
    None
    """

    possible_word_directions = []

    if difficulty == Difficulty.easy:
        possible_word_directions = [
            WordDirection.vertical, WordDirection.horizontal]
    else:
        possible_word_directions = [WordDirection.vertical,
                                    WordDirection.horizontal, WordDirection.diagonal]

    # Erstellen eines leeren Gitters
    grid = [[" "] * width for _ in range(height)]

    alphabet = generate_alphabet(difficulty, words)

    grid = populate_grid(grid, alphabet, difficulty, width,
                         height, words, possible_word_directions)

    render(grid, words)


# Liest alle benötigten Werte aus den Beispieldateien ein und speichert sie in Variablen
with open("worte0.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

dimensions = lines[0].split()
height = int(dimensions[0])
width = int(dimensions[1])


# Entfernen von Zeilenumbrüchen an Wörtern
uncleaned_words = lines[2:]
words = []
for word in uncleaned_words:
    words.append(word.strip())


# Erstellen von drei Spielen mit aufsteigenden Schwierigkeitsstufen
create_game(Difficulty.easy, words, width, height)
create_game(Difficulty.medium, words, width, height)
create_game(Difficulty.hard, words, width, height)
