def jahangir(jahan):
    ab_pos = jahan.find('AB')
    if ab_pos != -1:
        if 'BA' in jahan[ab_pos+2:]:
            return 'YES'
    ba_pos = jahan.find('BA')
    if ba_pos != -1:
        if 'AB' in jahan[ba_pos+2:]:
            return 'YES'
    return 'NO'
vorodi = input()
print(jahangir(vorodi))