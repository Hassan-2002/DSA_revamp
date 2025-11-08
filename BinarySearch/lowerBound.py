# Implement Lower Bound
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
def lowerBound(arr : list[int], target : int) -> int:
    left, right = 0, len(arr)-1
    while left<right:
        mid = (left+right)//2
        if arr[mid]<target:
            left = mid+1
        elif arr[mid]>=target:
            right = mid
    return left
arr = [0,2,8,10,15,16]
lower = lowerBound(arr,7)
print(lower)