win = 0
lose = 0
draw = 0
sum = 0
for i in range(1,31):
    points = int(input())
    sum = points + sum
    if points == 3:
        win = win + 1
    elif points == 1:
        draw = draw +1
    else:
        lose = lose + 1
print(sum , win)