'''
Input: a List of integers
Returns: a List of integers
'''
import math
# return an array where each item is the product of all other items


def product_of_all_other_numbers(arr):
    # multiply all items in the array together
    mult_total = math.prod(arr)
    # create an array to save multiplications in
    result = [0] * len(arr)
    # iterate over the original array
    for i, val in enumerate(arr):
        # divide the mult_total by the current value
        # save the resulting number in the correct position of result
        result[i] = mult_total // val
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 7, 3, 4]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

print([7*3*4, 1*3*4, 1*7*4, 1*7*3])
