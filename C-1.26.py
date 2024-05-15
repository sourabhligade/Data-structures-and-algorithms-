Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used
in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”.








def intergerss(a,b,c):
    if a+b==c:
        return f"{a}+{b}=={c}"
    elif a==b-c:
        return f"{a}=={b}-{c}"
    elif a*b==c:
        return f"{a}*{b}==c"
    else:
        return "no artihmentic sequence found"
    

a=int(input('a'))
b=int(input('b'))
c=int(input('c'))
print(intergerss(a,b,c))
