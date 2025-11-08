def rearrangeArray(nums: list[int]) -> list[int]:
        neg_list = []
        pos_list = []
        new_list = []*len(nums)
        for i in nums:
            if i <0:
                neg_list.append(i)
            else :
                pos_list.append(i)
        print(neg_list)
        print(pos_list)
        i,j=0,0
        while i < len(neg_list) and j < len(pos_list):
            
            new_list.append(pos_list[i])
            new_list.append(neg_list[i])
            i+=1
            j+=1
         
        return new_list 
nums = [3,1,-2,-5,2,-4]
answer = rearrangeArray(nums)
print(answer)