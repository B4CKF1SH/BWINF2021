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
    hotel_split = hotel.split()
    hotel_tupil.append((hotel_split[0], hotel_split[1]))

print(hotel_tupil)

val = []
wt = []
for hotel in hotel_tupil:
    val.append(float(hotel[0]))
    wt.append(float(hotel[1]))

print(val)
print(wt)

# Create the solver.
solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

values = val
weights = [wt]
capacities = [distance]

solver.Init(values, weights, capacities)
computed_value = solver.Solve()

packed_items = []
packed_weights = []
total_weight = 0
print('Total value =', computed_value)
for i in range(len(values)):
    if solver.BestSolutionContains(i):
        packed_items.append(i)
        packed_weights.append(weights[0][i])
        total_weight += weights[0][i]
print('Total weight:', total_weight)
print('Packed items:', packed_items)
print('Packed_weights:', packed_weights)


