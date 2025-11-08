def insertSort(nums:list) -> list :
        for i in range(len(nums)):
            j=i
            while j > 0 and nums[j]<nums[j-1]:
                  nums[j], nums[j-1] = nums[j-1],nums[j]
                  j-=1
        return nums
nums = [7,9,3,1,0,8,4,2]
print(insertSort(nums))