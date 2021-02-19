import itertools
def maximum_mismatches(s,n):
    if len(set(s)) == 1:
        return 0
    maxc = 0
    for str_c in set(itertools.permutations(s,n)):
        rev_str = str_c[::-1]
        counter = 0
        for i in range(n):
            if str_c[i] != rev_str[i]:
                counter += 1
        if maxc < counter:
            maxc = counter
    return maxc
s="aatacanaa"
print(maximum_mismatches(s,len(s)))