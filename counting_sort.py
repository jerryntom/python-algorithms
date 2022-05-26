def countingSort(arr):
    maxi = max(arr)

    count_array = [0] * (maxi + 1)

    for element in arr:
        count_array[element] += 1

    for i in range(0, maxi + 1):
        if count_array[i] != 0:
            print((str(i) + " ") * count_array[i], end="")


countingSort([10, 8, 7, 5, 4, 1, 0])
