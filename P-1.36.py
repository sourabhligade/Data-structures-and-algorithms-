#Write a Python program that inputs a list of words, 
#separated by white- space, and outputs how many times each word appears in the list.


from collections import Counter

user_input=input('enter a list of words serpreated by whitespaces').split()
counts=Counter(user_input)

for word,count in counts.items():
    print(f'{word}:{count}')
