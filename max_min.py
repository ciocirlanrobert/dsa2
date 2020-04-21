def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    length = len(ints)
    if length < 1:
        return None
    if length == 1:
        return (ints[0], ints[0])
    
    mini, maxi = ints[0], ints[0]
    
    for element in ints:
        if element > maxi:
            maxi = element
        if element < mini:
            mini = element
    
    return (mini, maxi)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if (-1,99) == get_min_max([-1,99,1,98,0]) else "Fail")
print("Pass" if (0,0) == get_min_max([0]) else "Fail")
print("Pass" if (-9,-5) == get_min_max([-5, -5, -6, -9, -5, -9]) else "Fail")
