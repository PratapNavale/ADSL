# Problem statement: Implement the problem statemnt of moving all zeros to end of the array.
# Description: Given an array of random numbers push all the zeros of the given array at the end of the array.

# Function to move all zeros to the end
def move_zeros_to_end(arr):
    n = len(arr)
    result = []

    # First, add all non-zero elements to the result
    for num in arr:
        if num != 0:
            result.append(num)

    # Count zeros and append them at the end
    zero_count = n - len(result)
    result.extend([0] * zero_count)

    return result


def main():
    n = int(input("Enter array size: "))
    arr = []

    print(f"Enter {n} elements:")
    for _ in range(n):
        arr.append(int(input()))

    print("Original array:")
    print(arr)

    result = move_zeros_to_end(arr)

    print("Zero appended to end of array:")
    print(result)


if __name__ == "__main__":
    main()
