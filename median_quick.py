import random


def findMedian(arr):
    maxi = max(arr)

    count_array = [0] * (maxi + 1)
    values = []

    for element in arr:
        count_array[element] += 1

    for i in range(0, maxi + 1):
        if count_array[i] != 0:
            values.extend(i for j in range(0, count_array[i]))

    if len(values) % 2 == 0:
        return (values[(len(values) // 2) - 1] + values[(len(values) // 2)]) / 2
    else:
        return values[(len(values) // 2)]


random_values = random.sample(range(0, 10000000), random.randint(1, 1000000))

print(findMedian(random_values))
