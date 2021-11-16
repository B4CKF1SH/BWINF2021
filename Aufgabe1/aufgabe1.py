# A G
# 2
# H 2
# I 5

vert = []
hori = []
hori_names = []

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


def free_right(place, ret):
    if hori[place] == 0:
        return ret
    elif place >= len(hori) - 3:  # Auto kann nicht aus dem Parkplatz herausgeschoben werden
        return None
    elif hori[place] == 1:
        x = [(hori_names[place], 1)]
        for a in ret:
            x.append(a)
        return free_right(place + 2, x)
    elif hori[place] == 2:
        x = [(hori_names[place], 2)]
        for a in ret:
            x.append(a)
        return free_right(place + 2, x)


def free_left(place, ret):
    if hori[place] == 0:
        return ret
    elif place <= 2:  # Auto kann nicht aus dem Parkplatz herausgeschoben werden
        return None
    elif hori[place] == 1:
        x = [(hori_names[place], 2)]
        for a in ret:
            x.append(a)
        return free_left(place - 2, x)
    elif hori[place] == 2:
        x = [(hori_names[place], 1)]
        for a in ret:
            x.append(a)
        return free_left(place - 2, x)


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
        if hori[auto] == 2:
            left = free_left(auto, [])
            if left is not None and len(left) <= 1:
                print_actions(auto, left, "links")
                continue
            right = free_right(auto, [])
        else:
            right = free_right(auto, [])
            if right is not None and len(right) <= 1:
                print_actions(auto, right, "rechts")
                continue
            left = free_left(auto, [])

        if left is None:
            actions = right
            direction = "rechts"
        elif right is None:
            actions = left
            direction = "links"
        elif len(right) <= len(left):
            actions = right
            direction = "rechts"
        else:
            actions = left
            direction = "links"

        if actions is None:
            print(chr(auto + vert_first) + ": unmöglich")
            continue
        else:
            print_actions(auto, actions, direction)


res()
