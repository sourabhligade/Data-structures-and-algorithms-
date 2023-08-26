# Write a short recursive Python function that finds the minimum and max- imum values in a sequence without using any loops.
def min_max_recursive(sequence,index=0):
    if index==len(sequence):
        return None,None
    
    current_val=sequence[index]

    if index==len(sequence)-1:
        return current_val,current_val
    
    min_rest,max_rest=min_max_recursive(sequence,index+1)
    min_val=min(current_val,min_rest)
    max_val=max(current_val,max_rest)

    return min_val,max_val


sequence = [3, 9, 1, 90, 5]
min_val, max_val = min_max_recursive(sequence)
print("Minimum:", min_val)
print("Maximum:", max_val)




