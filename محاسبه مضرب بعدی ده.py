number = int(input())
if (number%10) == 0:
    print(number+10)
elif (number%10) == 1:
    print(number+9)
elif (number%10) == 2:
    print(number+8)
elif (number%10) == 3:
    print(number+7)
elif (number%10) == 4:
    print(number+6)
elif (number%10) == 5:
    print(number+5)
elif (number%10) == 6:
    print(number+4)
elif (number%10) == 7:
    print(number+3)
elif (number%10) == 8:
    print(number+2)
else:
    print(number+1)