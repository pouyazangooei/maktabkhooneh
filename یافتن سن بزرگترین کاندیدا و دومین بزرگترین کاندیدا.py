age = int(input())
second = age
maximum = age
lastmax = maximum
while age != -1:
    age = int(input())
    new = age
    if new > maximum:
        second = lastmax
        maximum = new
        lastmax = maximum
    elif new < maximum and new > second:
        second = new
print(maximum , second)