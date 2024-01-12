class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uset1 = set()
        uset2 = set()
        count = 0

        for i in range(len(nums)):
            if not nums[i] in uset1:
                uset1.add(nums[i])
                
                nums[count] = nums[i]
                count += 1
            else:
                if not nums[i] in uset2:
                    uset2.add(nums[i])
                    
                    nums[count] = nums[i] 
                    count += 1                   
        return count