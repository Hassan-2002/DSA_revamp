#check if the array is rotated and sorted 
#the main idea to solve this is is to circularly loop around the array
#we maintain a counter if count=0 array is sorted and not rotated if count=1 array is sorted and rotated once 
#but if count>1 array is neither sorted nor rotated


def check(nums : list[int]) -> bool:
    n = len(nums)
    count = 0 
    for i in range(n):
        if nums[i] > nums[(i+1)%n]: #here is the tricky part. The %n part divided the index and circularly checks the index
            count+=1
            if count>1:
                return False
    return True 
 
    







