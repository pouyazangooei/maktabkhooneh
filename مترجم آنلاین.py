words_counter = int(input())
count = 1
Dict = {}
while count <= words_counter :
    count += 1
    words_and_meaning = str(input())
    list_wm = words_and_meaning.split()
    Dict [list_wm[0]] = list_wm[1]
sentence = str(input())
list_sentence = sentence.split()
for i in range(0,len(list_sentence)) :
    if list_sentence[i] in Dict :
        list_sentence[i] = Dict[list_sentence[i]]
print(' '.join(list_sentence))