Write a short Python function that takes a 
positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.




def sumofsquares(n):
    result = sum(i**2 for i in range(1,n,2))
    return result
    
print(sumofsquares(5))
