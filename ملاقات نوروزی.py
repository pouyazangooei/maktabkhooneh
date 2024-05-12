positions = input()
positions = positions.split()
positions = [eval(i) for i in positions]
positions.sort()
best = (positions[1] - positions[0]) + (positions[2] - positions[1])
print(best)