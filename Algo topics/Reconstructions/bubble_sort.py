### BUBBLE SORT
# Swap every pair iteratively till array is sorted
# O(n^2)
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    n = len(arr)
    swapped = True
    
    end = n - 1
    while swapped:
        swapped = False 
        
        for i in range(end):
            j = i + 1
            if arr[i] > arr[j]:
                swapped = True
                swap(i, j)
                
        # expecting the biggest value at the end
        end -= 1
        
    return arr