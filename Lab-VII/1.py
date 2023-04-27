def partition(arr, L, H):
    i = (L-1)
    p = arr[H]
    for j in range(L, H):
        if arr[j] <= p:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[H] = arr[H], arr[i+1]
    return (i+1)

def quickSort(arr, L, H):
    print(arr)
    if len(arr) == 1:
        return arr
    elif L < H:
        pi = partition(arr, L, H)
        quickSort(arr, L, pi-1)
        quickSort(arr, pi+1, H)

print("----------------------------------------------------------")
print("                      Quick Sort")
print("----------------------------------------------------------")
n=int(input("Enter no. of elements in array : "))
arr=[]
for i in range(0,n):
    a=int(input("Enter the element : "))
    arr.append(a)
print("\nGiven array is :",arr)
quickSort(arr, 0, n-1)
print("\nSorted array is :",arr)