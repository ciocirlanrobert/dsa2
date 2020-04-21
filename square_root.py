def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    start_index = 0
    end_index = number // 2
    highest_smaller = 0
    
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if mid * mid == number:
            return mid
        
        if mid * mid < number:
            start_index = mid + 1
            highest_smaller = mid
        else:
            end_index = mid - 1
    
    return highest_smaller

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (8 == sqrt(65)) else "Fail")
print("Pass" if (3513 == sqrt(12345678)) else "Fail")
