#A common punishment for school children is to write out a sentence mul- tiple times. Write a Python stand-alone program 
#that will write out the following sentence one hundred times: “I will never spam my friends again.”
#Your program should number each of the sentences and it should make eight different random-looking typos.


import random

sentence='I will never spam my friends again.'

for i in range(1,101):
  typo_count=0
  print(f'{}',end='')

  
  for char in sentence:
    if random.random()<0.08 and typo_count<8:
      typo=random.choice([typo.upper(),typo.lower()]
      print(typo,end='')
      typo_count+=1
    else:
      print(char,end='')

  print()
