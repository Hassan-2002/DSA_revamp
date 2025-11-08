#given two arrays arr 1 and arr 2. sort arr 1 in such a way that the elements also present in arr 2 are not sorted rather prepended to the sorted elements
from collections import Counter
def sortedArray(arr1 : list[int],arr2:list[int]) -> list[int]:
    count = Counter(arr2)
    j=0
    for num in arr1:
        if num in count and count[num] > 0:
            arr1.remove(num)
            arr1.insert(j,num)
            j += 1
            count[num] -= 1
    new_arr = sorted(arr1[j:])

    return arr1[:j]+new_arr  
arr1 = [5,68468,54,74,54,8,65,456,4,3,5,3,3,3]
arr2 = [5,3,3,4]
print(sortedArray(arr1,arr2))