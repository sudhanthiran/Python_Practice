def maxOnes(list):
    if(len(list)==1):
        return 0
    else:
        max_sum =0
        a=[]
        for count,ele in enumerate(list):
            temp = sum(ele)
            if(temp >= max_sum):
                max_sum=temp
                a.append(calc_max_ones(ele))
            else:
                a.append(0)
        return a.index(max(a))

def calc_max_ones(list):
    count_one =0
    for i in list:
        if i == 0:
            break
        else:
            count_one = count_one + 1
    return count_one


array = [[1,0,1,1,1,0,1],[1,1,1,1,0,1,0,0]] #[1]

print(maxOnes(array))

