age = int(input())
compare = age
while age != -1:
    age = int(input())
    if age > compare:
        compare = age
print(compare)