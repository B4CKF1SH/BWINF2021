# pro Tag 6 Stunden Fahrt (360 min), insgesamt max 5 Tage (5 * 360 = 1800) | 5 Nächte = 5 Hotels
# niedrigste Bewertung soll so hoch wie möglich sein

# 12        Anzahl der Hotels
# 1680      Gesamtfahrtzeit
# 12 4.3    Entfernung vom Start | Bewertung des Hotels
# 326 4.8
# 347 2.7
# 359 2.6
# 553 3.6
# 590 0.8
# 687 4.4
# 1007 2.8
# 1008 2.6
# 1321 2.1
# 1360 2.8
# 1411 3.3

from ortools.algorithms import pywrapknapsack_solver

with open("hotels1.txt") as f:
    lines = f.readlines()

num_hotels = lines[0]
distance = int(lines[1])

hotels = lines[2:len(lines)]
hotel_tupil = []
for hotel in hotels:
    dis, rat = hotel.strip().split()
    hotel_tupil.append((int(dis), float(rat)))

print(hotel_tupil)


def brute_force():
    highest = 0.0
    hotels = []

    for a in range(0, len(hotel_tupil)):
        a_dis, a_rat = hotel_tupil[a]
        for b in range(a+1, len(hotel_tupil)):
            b_dis, b_rat = hotel_tupil[b]
            if b_dis - a_dis >= 360:  # Maximal 6h Zeit pro Tag
                continue
            for c in range(b+1, len(hotel_tupil)):
                c_dis, c_rat = hotel_tupil[c]
                if c_dis - b_dis >= 360:  # Maximal 6h Zeit pro Tag
                    continue
                for d in range(c+1, len(hotel_tupil)):
                    d_dis, d_rat = hotel_tupil[d]
                    if d_dis - c_dis >= 360:  # Maximal 6h Zeit pro Tag
                        continue
                    for e in range(d+1, len(hotel_tupil)):
                        e_dis, e_rat = hotel_tupil[e]
                        if e_dis - d_dis >= 360:  # Maximal 6h Zeit pro Tag
                            continue

                        # print([(a_dis, a_rat), (b_dis, b_rat), (c_dis, c_rat), (d_dis, d_rat), (e_dis, e_rat)])
                        min_rat = min([a_rat, b_rat, c_rat, d_rat, e_rat])#
                        if min_rat >= highest:
                            highest = min_rat
                            hotels = [a, b, c, d, e]

    print(highest)
    print(hotels)

brute_force()