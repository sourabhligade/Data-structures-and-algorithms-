#Give a single command that computes the sum from Exercise R-1.4, 
rely- ing on Python’s comprehension syntax and the built-in sum function.







def sumofsquares(n):
    result = sum(i**2 for i in range(1, n))
    return result
    
print(sumofsquares(5))
