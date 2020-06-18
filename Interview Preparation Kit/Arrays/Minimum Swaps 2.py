# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
# For example, given the array arr=[7, 1, 3, 2, 4, 5 , 6] we perform the following steps:
# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took 5  swaps to sort the array.
#
# Function Description
# Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
# minimumSwaps has the following parameter(s):
# arr: an unordered array of integers
# Input Format
# The first line contains an integer,n, the size of arr.
# The second line contains n space-separated integers arr[i].
#
# Sample Input 0
# 4
# 4 3 1 2
# Sample Output 0
# 3


def minimumSwaps(arr: list) -> int:
    # First solution, but not work with big data, failed by timeout:
    # s_arr, count = sorted(arr), 0
    # for i in arr:
    #     if arr.index(i) != s_arr.index(i):
    #         count += 1
    #         first_index = arr.index(i)
    #         second_index = arr.index(s_arr[first_index])
    #         arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
    # return count

    # Second solution:
    count = 0
    sarr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sarr[i]:

            # temp = arr[i]
            #
            # arr[i] = arr[arr.index(i + 1)]
            #
            # arr[arr.index(i + 1)] = temp

            arr[i], arr[arr.index(sarr[i])] = arr[arr.index(sarr[i])], arr[i]

            count += 1
    print(count)
    return count -1







# Test cases:
assert minimumSwaps(arr=[4, 3, 1, 2]) == 3
assert minimumSwaps(arr=[1, 3, 5, 2, 4, 6, 7]) == 3


