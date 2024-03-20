def selection_sort(unsorted: list[int]):
    arr = unsorted
    
    for i in range(len(arr)):
        min_num_idx = i
        for j in range(i, len(arr)):
            if arr[min_num_idx] > arr[j]:
                min_num_idx = j
        
        arr[i], arr[min_num_idx] = arr[min_num_idx], arr[i]

    return arr
