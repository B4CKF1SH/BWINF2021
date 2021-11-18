# 6
# 10 3
# 50 2
# 100 3
# 500 3
# 1000 3
# 5000 1

with open("gewichtsstuecke0.txt", 'r') as f:
    lines = f.readlines()

count = int(lines[0].strip())
weights = []

for i in range(1, count + 1):
    weight, num = map(int, lines[i].strip().split(" "))
    weights.append((weight, num))


combinations = []  # [(10, ([w, w, w], []))]


def append_c(c):
    c_weight, c_arr = c
    c_l, c_r = map(len, c_arr)
    c_length = c_l + c_r
    for i in range(len(combinations)):
        a = combinations[i]
        a_weight, a_arr = a
        if a_weight == c_weight:
            a_l, a_r = map(len, c_arr)
            a_length = a_l + a_r
            if a_length <= c_length:
                return
            else:
                combinations.pop(i)
                combinations.append(c)
                return
    combinations.append(c)


for w in weights:
    weight, num = w
    combos = []
    for c in range(0, num + 1):
        l = []
        for i in range(c):
            l.append(weight)
        combos.append((- c * weight, (l, [])))
        if not c == 0:
            combos.append((c * weight, ([], l)))

    to_append = []
    for c in combos:
        # c = (-100, ([50, 50], []))
        c_weight, c_arr = c
        c_l, c_r = c_arr

        for a in combinations:

            d_l = c_l.copy()
            d_r = c_r.copy()
            a_weight, a_arr = a
            if a == c:
                continue
            a_l, a_r = a_arr

            for x in a_l:
                d_l.append(x)
            for x in a_r:
                d_r.append(x)

            to_append.append((c_weight + a_weight, (d_l, d_r)))

    for c in combos:
        append_c(c)
    for t in to_append:
        append_c(t)

i = 0
while i < len(combinations):
    c = combinations[i]
    c_weight, c_arr = c
    c_l, c_r = c_arr

    if c_weight < 0:
        combinations.pop(i)
    elif c_weight > 20000:
        combinations.pop(i)
    else:
        i += 1


for t in range(1, 1001):
    target = t*10  # Zielgewicht (10er-Schritte)

    closest_dif = 9999999999999999999999999999999
    closest = ()
    for c in combinations:
        c_weight, _ = c
        dif = target - c_weight
        dif = max(dif, -dif)
        if dif < closest_dif:
            closest_dif = dif
            closest = c

    c_weight, c_arr = closest
    l, r = c_arr
    if closest_dif == 0:
        print(str(target) + "g: Erreichbar. Links: " + str(l) + " Rechts: " + str(r))
    else:
        print(str(target) + "g: Unerreichbar. Nächstes: " + str(c_weight))
