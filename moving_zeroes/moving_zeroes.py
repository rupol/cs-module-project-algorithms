'''
Input: a List of integers
Returns: a List of integers
'''
# return the array with all non-zero integers to the left


def moving_zeroes(arr):
    # loop through the array
    for i, val in enumerate(arr):
        # if val is not 0, remove from current position and insert at the front of the array
        if val != 0:
            arr.insert(0, arr.pop(i))
    # return sorted array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
