def divisor(a):
    count = 0
    for n in range(1,a+1):
        if a % n == 0:
            count = count + 1
    final_count = count
    return final_count
last_count = 0
last_number = 0
for i in range(1,21):
    number = int(input())
    count = divisor(number)
    if count > last_count:
        last_count = count
        last_number = number
    elif count == last_count and number > last_number:
        last_number = number
print (last_number , last_count)