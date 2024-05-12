tedad_niaz = int(input())
tedad_sherkat = input()
tedad_sherkat = tedad_sherkat.split()
tedad_sherkat = [eval(i) for i in tedad_sherkat]
count = 0
for i in range(0,3) :
    count += tedad_sherkat.count(i)
count = count // 3
print(count)