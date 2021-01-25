# cook your dish here
import itertools
T= int(input())
while (T > 0):
    secondline = input()
    data = input()
    N,K,P = secondline.split(" ")
    data = list(data.split(" "))
    data.sort()
    working_set=list(itertools.combinations(data,int(K)))
    l = len(working_set)
    diff = []
    count = 0
    for i in working_set:
        diff.append([])
        for j in range(0, len(i)):
            for k in range(0, len(i)):
                difference = int(i[j]) - int(i[k])
                index = working_set.index(i)
                diff[index].append(difference)
    print(len(diff))
    for i in diff:
        if all(x <= int(P) for x in i):
            count += 1
    print(count)

    T -= 1