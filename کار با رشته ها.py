strr = str(input())
strr = strr.lower()
new_str = ''
for i in range (0,len(strr)):
    if strr[i:i+1] != 'a' and strr[i:i+1] != 'e' and strr[i:i+1] != 'i' and strr[i:i+1] != 'o' and strr[i:i+1] != 'u' :
        picked = strr[i:i+1]
        new_str = new_str + strr[i:i+1]
last_str = ''
for i in range (0,len(new_str)):
    pick = '.' + new_str[i:i+1]
    last_str = last_str + pick
print(last_str)