def bubbleSort(nums:list )-> list:
    n = len(nums)-1
    swap = 0
    while n>0:
        for i in range(n):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
                swap+=1
        if swap == 0:
            return nums 
        n-=1
    return nums
nums = [7,9,3,1,0,8,4,2]
print(bubbleSort(nums))