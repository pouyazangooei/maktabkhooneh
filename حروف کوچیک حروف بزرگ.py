users_input = input()
upcount = 0
lowcount = 0
for i in range(0,len(users_input)) :
    if users_input[i:i+1] == users_input[i:i+1].upper() :
        upcount += 1
    elif users_input[i:i+1] == users_input[i:i+1].lower() :
        lowcount += 1
if upcount > lowcount :
    print(users_input.upper())
else :
    print(users_input.lower())