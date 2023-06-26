R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, 
in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.


  def minmax(data):
    smallest = largest = data[0]  # Initialize smallest and largest to the first element of the sequence
    for num in data:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return (smallest, largest)

numbers = [3, 1, 7, 2, 9, 4]
result = minmax(numbers)
print(result) 
