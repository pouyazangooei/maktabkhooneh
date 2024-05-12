takhte = str(input())
number_one = ''
number_two = ''
number_three = ''
for i in range (0,len(takhte)) :
    temp = takhte[i:i+1]
    if temp == '1' :
        number_one = number_one + '1+'
    elif temp == '2' :
        number_two = number_two + '2+'
    elif temp == '3' :
        number_three = number_three + '3+'
final_numb = number_one + number_two + number_three
print (final_numb[:-1])