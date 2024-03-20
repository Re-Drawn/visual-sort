def insertion_sort(unsorted):
    arr = unsorted

    for i in range(1, len(arr)):
        element = arr[i]
        
        for j in range(i-1, -1, -1):
            if element >= arr[j]:
                break
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
