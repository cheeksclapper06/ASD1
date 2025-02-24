def bubble_sort(arr):
    compares = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            compares += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return compares, swaps

def modified_bubble_sort(arr):
    compares = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            compares += 1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
        if not swapped:
            break
    return compares, swaps

def comb_sort(arr):
    n = len(arr)
    gap = n
    is_swapped = True
    compares = 0
    swaps = 0
    while gap != 1 or is_swapped:
        is_swapped = False
        gap = int(gap / 1.3)
        if gap <= 1:
            gap = 1
        for i in range(0, n - gap):
            compares += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swaps += 1
                is_swapped = True
    return compares, swaps
