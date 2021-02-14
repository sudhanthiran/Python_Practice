def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

