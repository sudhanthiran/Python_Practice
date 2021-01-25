T=int(input())
for i in range(0,T):
    N = int(input())
    p = []
    p = input().split()
    people = 0
    handshake = []
    totalhandshake = 0
    for i in range(0, N):
        #print(i)
        #print(people)
        #print(p[i])
        if (i != 0):
            handshake.append(people * int(p[i]))
        if (i == 0):
            handshake.append(0)
        totalhandshake += int(handshake[i])
        people += int(p[i])
        #print(handshake)
    print(totalhandshake)