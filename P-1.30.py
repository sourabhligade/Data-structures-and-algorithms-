#Write a Python program that can take a positive integer
#greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.





def integerGreat(num):
    count=0
    while num>=2:
        num/=2
        count+=num
        return count
    num=input('Enter number greter than or equal to 2')

print(integerGreat(32))
