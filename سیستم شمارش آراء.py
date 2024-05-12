from collections import OrderedDict
c_quantities = int(input())
count = 1
Dict = OrderedDict()
while count <= c_quantities :
    count += 1
    c_names = str(input())
    if c_names in Dict :
        Dict [c_names] += 1
    else :
        Dict [c_names] = 1
for names in sorted(Dict.keys()) :
    print(names,Dict[names])