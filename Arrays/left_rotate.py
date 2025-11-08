def rotate(nums):
    first_elem = nums[0]
    i,j =0,1
    while j < len(nums):
        nums[i] = nums[j]
        i+=1
        j+=1
    nums[-1] = first_elem
    print(nums)
nums = [1,2,3,4]
rotate(nums)