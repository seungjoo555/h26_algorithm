ns = [15,7,43,9,53,3,23]

def quick_sort(A, left, right):
    print(left, right)
    if left < right:
        pivot = A[left]
        mid = (left+right)//2
        low = left + 1
        high = right
        
        while low <= high:
            while low <= high and A[low] < pivot: low += 1
            while low <= high and A[high] > pivot: high -= 1

            if low < high:
                A[low], A[high] = A[high], A[low]
            else:
                break
        
        A[left], A[high] = A[high], A[left]

        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)


quick_sort(ns, 0, len(ns)-1)
print(ns)