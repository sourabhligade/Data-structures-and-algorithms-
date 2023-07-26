\
C-1.14 Write a short Python function that takes a sequence of integer values and determines 
if there is a distinct pair of numbers in the sequence whose product is odd.


def hasDistinctOddProduct(sequence):
    odd_numbers=set()

    
    for num in sequence:
      if num %2!=0:
        if any((num * other_num)%2!=0 for other_num in sequence):
            return True
        odd_numbers.add(num)
    return False

sequene=[1, 2, 3, 4, 5]
print(hasDistinctOddProduct(sequence))
    
