def recursion(n):
    if n == 0:
        return 0
    return n + recursion(n - 1)

print(recursion(5))
"""
1. 5 + recursion(4)
2. 5 + (4 + recursion(3))
3. 5 + (4 + (3 + recursion(2)))
4. 5 + (4 + (3 + (2 + recursion(1))))
5. 5 + (4 + (3 + (2 + (1 + recursion(0)))))
6. 5 + (4 + (3 + (2 + (1 + 0))))
7. 15
"""
#example on how callback stack works
"""
'friends.'      ==> 'friends.'
'my' + c()      ==> 'my' + 'friends.' == 'my friends.'
'hello' + b()   ==> 'hello' + 'my friends' == 'hello my friends'
"""
def a():
    return "hello " + b()
def b():
    return "my " + c()
def c():
    return "friends."

print(a())

#exercise: string reversal with recursion
def string_reversal(string):
    #What is my base condition?
    if string == "":
        return ""
    #What is the smallest amount of work I can do in each iteration?
    return string_reversal(string[1:]) + string[0]
"""
1. string_reversal("ello") + "h"
2. (string_reversal("llo") + "e" ) + "h"
3. ((string_reversal("lo") + "l" ) + "e" ) + "h"
4. (((string_reversal("o") + "l" ) + "l" ) + "e" ) + "h"
5. ((((string_reversal("") + "o" ) + "l" ) + "l" ) + "e" ) + "h"
6. (((("" + "o" ) + "l" ) + "l" ) + "e" ) + "h"
7. "olleh"
"""
print(string_reversal("hello"))

#exercise: palindrome word with recursion

def palindrome(string):
    #base-case if and stopping condition
    if len(string) == 0 or len(string) == 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])

    return False

print(palindrome("detartrated"))