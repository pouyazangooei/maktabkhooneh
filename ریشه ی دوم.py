import math
quantities = int(input())
inputs = []
for i in range(quantities) :
    transf = math.sqrt(int(input()))
    result = int(transf*10000)/10000
    inputs.append(result)
for a in inputs :
    print(f"{a:.4f}")