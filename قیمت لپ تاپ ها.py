def check_laptops(n, laptops):
    for i in range(n):
        for j in range(n):
            if laptops[i][0] < laptops[j][0] and laptops[i][1] > laptops[j][1]:
                return "happy irsa"
    return "poor irsa"
n = int(input())
laptops = []
for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))
print(check_laptops(n, laptops))