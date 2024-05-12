number = int(input())
count = 0
for i in range(1,number):
    if (number % i) == 0:
        count = count + 1
if count > 1:
    print('not prime')
elif number == 1:
    print('not prime')
elif number == 2:
    print('prime')
else:
    print('prime')