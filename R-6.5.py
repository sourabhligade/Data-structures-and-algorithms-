#Implementafunctionthatreversesalistofelementsbypushingthemonto
#a stack in one order, and writing them back to the list in reversed order.


def reverseList(my_list):
    Temp_stack=[]
    for item in my_list:
        Temp_stack.append(item)

    reversed_list=[]
    while Temp_stack:
        reversed_list.append(Temp_stack.pop())

    return reversed_list


original_list = [1, 2, 3, 4, 5]
reversed_list = reverseList(original_list)
print(reversed_list) 
