import random
S1 = 1
B1 = 99
computer_guess = random.randint(S1,B1)
print('Ai guess is:',computer_guess)
my_idea = input()
while my_idea != 'd':
    if my_idea == 'k':
        B1 = computer_guess - 1
        computer_guess = random.randint(S1,B1)
        print('Ai guess is:',computer_guess)
        my_idea = input()
    elif my_idea == 'b':
        S1 = computer_guess + 1
        computer_guess = random.randint(S1,B1)
        print('Ai guess is:',computer_guess)
        my_idea = input()
print('yes my idea was:',computer_guess)