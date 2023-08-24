#Write a short recursive Python function that takes a character string s and outputs its reverse. For example, the reverse of pots&pans would be
#snap&stop .

def reverse_string(s):
    if len(s)<=1:
        return s
    return s[-1]+reverse_string(s[:-1])


s='snap&stop '
print(reverse_string(s))
