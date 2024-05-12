users_input = input()
users_input = users_input.lower()
reverse_input = ''
for i in range(0,len(users_input)) :
    reverse_input = users_input[i:i+1] + reverse_input
if reverse_input == users_input:
    print('palindrome')
else:
    print('not palindrome')