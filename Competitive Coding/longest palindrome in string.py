def palindrome(list_b):
    longest_palindrom = ''
    for i in list_b:
        if(i == i[::-1]):
            if(len(i)> len(longest_palindrom)):
                longest_palindrom = i

    print(longest_palindrom)


a= "abcdcba"


list_a =[]


for i in range(1,len(a)-1):
    list_a.append(a[i::1])

for i in range(1,len(a)-1):
    list_a.append(a[i::-1])

if (a == a[::-1]):
    print(a)
else:
    palindrome(list_a)

#print(list_a)