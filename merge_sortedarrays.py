def merge_sorted_arrays(array1, array2):
    if len(array1) == 0:
        return array2

    if len(array2) == 0:
        return array1

    merged_array = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):   # O(a + b) for the worst case (a = len(array1) and b = len(array2))
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            merged_array.append(array2[j])
            j += 1
        elif array1[i] == array2[j]:
            merged_array.append(array1[i])
            i += 1
            j += 1

    if i == len(array1):
        merged_array = merged_array + array2[j:]

    elif j == len(array2):
        merged_array = merged_array + array1[i:]

    return merged_array


if __name__ == '__main__':
    result = merge_sorted_arrays([0, 3, 4, 31], [3, 4, 6, 30])      # O(n + m)
    print(result)

    # method 2
    lst1 = [1, 3, 5]
    lst2 = [2, 4, 6]
    lst3 = sorted(lst1 + lst2)
    print(lst3)
