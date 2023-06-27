#Demonstrate how to use Python’s list comprehension syntax to produce 
thelist[ a , b , c ,..., z ],butwithouthavingtotypeall26such characters literally.



import string
alphabet_sequence=[char for char in string.ascii_lowecase]
print(alphabet_sequence)
