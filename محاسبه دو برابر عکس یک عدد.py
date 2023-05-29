number = int(input())
if number>=100 and number<=999:
    output = str(number % 10) + str( (number // 10) % 10 ) + str(number // 100)
    print( int(output)*2 )
else:
    print('3 Raqami Nist!')