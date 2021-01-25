def maxOnes(list):
    if(len(list)==1):
        return 0
    else:
        max_sum =0
        idx=None
        for count,ele in enumerate(list):
            temp = sum(ele)
            if(temp > max_sum):
                max_sum=temp
                idx = count
        return idx

# all 1 comes before 0 by this we can just calculate the sum

array = [[1,1,1,1,0,0],[1,1,1,1,0,0,0,0]] #[1]

print(maxOnes(array))

