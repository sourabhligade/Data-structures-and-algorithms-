R-1.4 Write a short Python function that takes a positive integer n and 
returns the sum of the squares of all the positive integers smaller than n.




def sumofsquares(n):
    sum=0
    for i in range(1,n):
        sum+=i**2
        print(sum) 
results=sumofsquares(5)
print(results)
