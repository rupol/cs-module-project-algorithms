'''
Input: an integer
Returns: an integer
'''
import functools


# return the number of ways n cookies can be eaten if cookies can be eaten one, two, or three at a time
# memoization
@functools.lru_cache()
def eating_cookies(n):
    # base cases
    # 0 ways to eat negative cookies
    if n < 0:
        return 0
    # 1 way to eat 0 cookies
    if n == 0:
        return 1
    # recursive case
    # eating 3 cookies, eating 2 cookies, eating 1 cookie
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
