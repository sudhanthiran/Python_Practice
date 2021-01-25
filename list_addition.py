list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]

list1.append(34)

print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

list1.append(34)

# Contents of list1 are same as above
# program, but contents of list2 are
# different.
print(list1)
print(list2)