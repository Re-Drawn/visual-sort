def selection_sort(unsorted: list[int]):
    comparisons = []
    swaps = []
    arr = unsorted
    
    for i in range(len(arr)):
        min_num_idx = i
        for j in range(i, len(arr)):
            comparisons.append((j, min_num_idx))
            if arr[min_num_idx] > arr[j]:
                min_num_idx = j
        comparisons.append((i, min_num_idx))
        swaps.append((i, min_num_idx))
        arr[i], arr[min_num_idx] = arr[min_num_idx], arr[i]

    return arr, comparisons, swaps
