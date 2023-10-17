#Give a recursive method for removing all the elements from a stack.
def clear_stack(stack):
    if not stack:
        return
    stack.pop()
    clear_stack(stack)


my_stack=[]
my_stack.append(2)
my_stack.append(4)
my_stack.append(6)
clear_stack(my_stack)
print(my_stack)

