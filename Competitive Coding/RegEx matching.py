"""
Given a pattern string and a test string, Your task is to implement RegEx substring matching.
If the pattern is preceded by a ^, the pattern(excluding the ^) will be matched with
the starting position of the text string. Similarly, if it is preceded by a $, the
pattern(excluding the ^) will be matched with the ending position of the text string.
If no such markers are present, it will be checked whether pattern is a substring of test.

Example :
^coal
coaltar
Result : 1
tar$
coaltar
Result : 1
rat
algorate
Result: 1
abcd
efgh
Result :0

Input: The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. Each test case contains two lines.
The first line of each test case contains a pattern string.
The second line of each test case consists of a text string.

Output: Corresponding to every test case, print 1 or 0 in a new line.

Constrains:
1<=T<=100
1<=length of the string<=1000
"""
def isSubString(test_string,base_string):
    flag = base_string.find(test_string)
    if(flag == -1):
        return False
    else:
        return True

def test_for_regex():
    test_string = str(input())
    base_string = str(input())
    flag=False
    if (test_string.startswith('^')):
        flag = (test_string[1:] == base_string[:len(test_string)-1])
    elif(test_string.endswith('$')):
        flag = (test_string[:len(test_string)-1] == base_string[(len(test_string)-1)*-1:])
    else:
        flag = (isSubString(test_string, base_string))
    if(flag==True):
        print("1")
    else:
        print("0")

t = int(input())

for i in range(t):
    test_for_regex()