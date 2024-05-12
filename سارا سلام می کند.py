typing = input()
the_word = 'hello'
new_str = ''
for i in range(len(typing)):
    checking = typing[i:i+1]
    if checking in the_word:
        new_str = new_str + checking

index = 0
for char in new_str:
    if index < len(the_word) and char == the_word[index]:
        index += 1

if index == len(the_word):
    print('YES')
else:
    print('NO')
