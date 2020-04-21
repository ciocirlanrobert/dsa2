def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        

    return merged


def rearrange_digits(input_list):
    if len(input_list) == 1 or len(input_list) == 0:
        return None
    
    nr1,nr2 = 0,0
    input_list = mergesort(input_list)
    length = len(input_list) - 1
    for index in range(length, -1, -1):
        if index % 2 == 0:
            nr1 = nr1*10 + input_list[index]
        else:
            nr2 = nr2*10 + input_list[index]
            
    return [nr1, nr2]
            
        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[1,2,2], [22, 1]]
test_function(test_case)

test_case = [[9, 0, 0, 1, 1, 1], [910, 110]]
test_function(test_case)

test_case = [[5, 1], [5, 1]]
test_function(test_case)
