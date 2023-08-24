#Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse. For example,   racecar   and
#gohangasalamiimalasagnahog   are palindromes.


def ispalindrome(s):
    if len(s)<=1:
        return True
    if s[0]==s[-1]:
        return ispalindrome(s[1:-1])
    else:
        return False
    
s='racecar'
print(ispalindrome(s))

    
