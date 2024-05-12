final_name = []
for i in range(10) :
    names = str(input())
    names = names.lower()
    names = names[0].upper() + names[1:]
    final_name.append(names)
for names in final_name :
    print(names)