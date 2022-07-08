li = [6, 3, 4, 8, 9, 5, 1, 7, 2]


def insert_sort(li, rightIndex, i):
    j = rightIndex
    for i in range(len(li)):
        j = i
        while j > 0:
            li[j] = li[j - 1]
            j -= 1
        if j = 0 or li[j - 1] <= li[j]:
            return None

    return


insert_sort(li)
print(insert_sort(li))
