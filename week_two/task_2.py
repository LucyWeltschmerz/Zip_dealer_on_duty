def find_missing_integer(arr):
    arr.sort()

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1


arr_1 = [1, 2, 4, 5, 6]
print((find_missing_integer(arr_1)))
