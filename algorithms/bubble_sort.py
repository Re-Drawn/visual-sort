def bubble_sort(unsorted: list[int]):
    comparisons = []
    swaps = []
    arr = unsorted

    for i in range(len(arr)):
        sorted = True

        for j in range(len(arr)-i-1):
            comparisons.append((j, j+1))
            if arr[j] > arr[j+1]:
                swaps.append((j, j+1))
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        
        if sorted: 
            break
    
    return arr, comparisons, swaps