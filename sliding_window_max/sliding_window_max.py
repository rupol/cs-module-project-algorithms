'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# return an array with the max value of each window (i to i + k)


def sliding_window_max(nums, k):
    # create an array to save the max values in
    result = [0] * (len(nums) - (k - 1))
    # iterate through the array
    for i in range(len(nums)):
        # if i is k items from the end of the array
        if i + k <= len(nums):
            # slice out a window from i to i + k
            window = nums[i:i+k]
            # find the max of that subarray
            result[i] = max(window)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
