# A G
# 2
# H 2
# I 5

vert = []
hori = []
hori_names = []

# Einlesen der Daten
with open("parkplatz0.txt", "r") as f:
    lines = f.readlines()

    row_1 = lines[0].strip()
    first, last = row_1.split(" ")
    vert_first = ord(first)  # Speichern des ersten Buchstabens für spätere Umrechnung
    x = 0
    for i in range(ord(first), ord(last) + 1):
        vert.append(x)
        hori.append(0)
        hori_names.append("")
        x += 1

    num_hori = int(lines[1])
    for i in range(num_hori):
        car = lines[2 + i].strip()
        name, pos = car.split(" ")
        pos = int(pos)
        hori[pos] = 1
        hori[pos + 1] = 2
        hori_names[pos] = name
        hori_names[pos + 1] = name


# Anzahl an Verschiebungen nach rechts
def free_right(place, ret):
    if hori[place] == 0:  # Falls der Platz leer ist, muss nicht mehr geschoben werden
        return ret
    elif place >= len(hori) or place >= len(hori) - 4 + hori[place]:  # Auto kann nicht aus dem Parkplatz herausgeschoben werden
        return None
    elif hori[place] == 1:  # Das Auto muss 1 Parkplatz nach rechts verschoben werden
        x = [(hori_names[place], 1)]
        for a in ret:
            x.append(a)
        return free_right(place + 2, x)  # Überprüfen des Parkplatzes, auf den das Auto geschoben wird
    elif hori[place] == 2:  # Das Auto muss 2 Parkplätze nach rechts verschoben werden
        x = [(hori_names[place], 2)]
        for a in ret:
            x.append(a)
        return free_right(place + 2, x)  # Überprüfen des Parkplatzes, auf den das Auto geschoben wird


# Anzahl an Verschiebungen nach links
def free_left(place, ret):
    if hori[place] == 0:  # Falls der Platz leer ist, muss nicht mehr geschoben werden
        return ret
    elif place <= -1 or place <= 3 - hori[place]:  # Auto kann nicht aus dem Parkplatz herausgeschoben werden
        return None
    elif hori[place] == 1:  # Das Auto muss 2 Parkplätze nach links verschoben werden
        x = [(hori_names[place], 2)]
        for a in ret:
            x.append(a)
        return free_left(place - 2, x)  # Überprüfen des Parkplatzes, auf den das Auto geschoben wird
    elif hori[place] == 2:  # Das Auto muss 1 Parkplatz nach links verschoben werden
        x = [(hori_names[place], 1)]
        for a in ret:
            x.append(a)
        return free_left(place - 2, x)  # Überprüfen des Parkplatzes, auf den das Auto geschoben wird


def print_actions(auto, actions, direction):
    out = chr(auto + vert_first) + ": "
    i = 0
    for action in actions:
        if not action:
            continue

        if i > 0:
            out += ", "
        else:
            i += 1

        car_name, amount = action
        out += car_name + " " + str(amount) + " " + direction

    print(out)


def res():
    for auto in vert:
        left = free_left(auto, [])
        right = free_right(auto, [])

        if left is None:  # Es kann nur nach rechts geschoben werden
            actions = right
            direction = "rechts"
        elif right is None:  # Es kann nur nach links geschoben werden
            actions = left
            direction = "links"
        elif len(right) <= len(left):  # Nach rechts muss weniger geschoben werden
            actions = right
            direction = "rechts"
        else:  # Nach links muss weniger geschoben werden
            actions = left
            direction = "links"

        if actions is None:  # Es kann nicht geschoben werden
            print(chr(auto + vert_first) + ": unmöglich")
            continue
        else:
            print_actions(auto, actions, direction)


res()
