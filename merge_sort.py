A = [5, 7, 23, 14, 9, 3, 59, 49]
new_list = [0]* len(A)
def merge(A, left, mid, right):
    if left == right:
        new_list[mid] = A[mid]
        return
    pL = pNew = left
    pR = mid+1
    while pL <= mid and pR <= right:
        if A[pL] < A[pR]:
            new_list[pNew] = A[pL]
            pL += 1
            pNew += 1
        else:
            new_list[pNew] = A[pR]
            pR+=1
            pNew += 1
    if pL <= mid:
        new_list[pNew:pNew+mid-pL+1] = A[pL:mid+1]
    elif pR <= right:
        new_list[pNew:pNew+right-pR+1] = A[pR:right+1]
    A[left:right+1] = new_list[left:right+1]

def merge_sort(A, left, right):
    if left >= right: return
    mid = (left+right) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid+1, right)
    merge(A, left, mid, right)
    print(left, right, new_list)

merge_sort(A, 0, len(A)-1)
print(A)