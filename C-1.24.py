Write a short Python function that counts the number of vowels in a given
character string.


def vowels(str):
  vowels='AEIOUaeiou'
  count=0
  for char in str:
    if char in vowels:
      count+=1
  return count



mystring=('Hello, to the world')
num=vowels(mystring)
print(num)
