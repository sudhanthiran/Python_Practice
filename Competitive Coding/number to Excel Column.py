def convertToTitle( n: int) -> str:
    c = n % 26
    print(c)
    S=""
    if (n>26):
        S= S+"A"+convertToTitle(c)
    elif (n >= 0 and n <= 26):
        S= S+ (chr(65+n-1))
    return S

print(convertToTitle(1))


