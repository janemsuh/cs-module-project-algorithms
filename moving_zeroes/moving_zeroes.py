'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zeroes_arr = []
    for idx, val in enumerate(arr):
        # add zero value indexes in arr to zeroes_arr
        if val == 0:
            zeroes_arr.append(idx)
    # print(zeroes_arr)
    
    for idx, val in enumerate(zeroes_arr):
        # remove zero from arr based on index (val in zeroes_arr = index of 0 in arr) saved in zeroes_arr
        # must subtract idx after each successive zero is moved
        arr.pop(val - idx)
        # print(f"val: {val}")
        # print(f"idx: {idx}")
        # print(f"val - idx: {val - idx}")

        # add zero to the end of arr
        arr.append(0)

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")