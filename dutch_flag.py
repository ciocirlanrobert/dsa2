def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    
    index0 = 0
    index2 = len(input_list) - 1
    start_index = 0
    
    while start_index <= index2:
        if input_list[start_index] == 0:
            input_list[start_index] = input_list[index0]
            input_list[index0] = 0
            start_index += 1
            index0 += 1
        elif input_list[start_index] == 2:
            input_list[start_index] = input_list[index2]
            input_list[index2] = 2
            index2 -= 1
        else:
            start_index += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1])
test_function([2])
test_function([0])
test_function([1,2,0])
