def binary_search(input_array, value):
    """Your code goes here."""
    mid = len(input_array)//2
    start=0
    end=len(input_array)-1
    for i in range(len(input_array)):
        print(start,mid,end)
        if input_array[mid] == value:
            return mid
        elif input_array[mid]<value:
            start =mid+1
            mid =(start+end)//2
        else:
            end =mid-1
            mid = (start +end)//2
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))