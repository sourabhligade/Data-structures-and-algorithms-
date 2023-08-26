
#C-4.10 Describe a recursive algorithm to compute
#the integer part of the base-two logarithm of n 
#using only addition and integer division.

def base_two(n):
    if n<=1:
        return 0
    else:
        return 1+base_two(n//2)
    

n=16
result=base_two(n)
print(result)
