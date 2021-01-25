def nearest(n: int):
    str_n = str(n)
    digit_2_add_or_sub = 0
    last_digit = int(str_n[len(str_n)-1])
    if(last_digit <=5):
        n = n - last_digit
    else:
        digit_2_add_or_sub = 10 - last_digit
    print(n+digit_2_add_or_sub)


T = int(input())

for i in range(T):
    N = int(input())
    nearest(N)
