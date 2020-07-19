'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort array
    arr.sort()

    # check index pairs (starting with 0)
    # if there is only one number OR
    # if current value <> next value in the sorted array
    # return current value
    for idx, val in enumerate(arr):
        if (idx == len(arr) - 1) or (idx % 2 == 0 and arr[idx] != arr[idx + 1]):
            return val

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")