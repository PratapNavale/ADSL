# Problem Statement: Implement a problem of number of zeros.
#   Description: Given an array of 1's and 0's which has all 1's fist followed by all zeros. Find the number of 0's and cout the number of zeros in an array.

a = input("Enter the binary number (only 1's followed by 0's allowed): ")

if all(ch in '01' for ch in a) and '01' not in a:
    zero_count = a.count('0')
    print("Number of zeroes is:", zero_count)
else:
    print("Invalid case")
