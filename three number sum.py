a= [12,3,1,2,-6,5,-8,6]
target_sum = 0
list =[]

for i in range(0,len(a)):
    for j in range(i.__index__()+1,len(a)):
        for k in range(j.__index__()+1,len(a)):
            sum = a[i]+a[j]+a[k]
            if (sum == target_sum):
                temp_list =[]
                temp_list.append(a[i])
                temp_list.append(a[j])
                temp_list.append(a[k])
                temp_list.sort()
                list.append(temp_list)

print(sorted(list))