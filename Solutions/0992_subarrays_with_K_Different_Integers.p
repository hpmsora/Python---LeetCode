class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def goodLessEqualK(nums, k):
            dist=0
            freq=[0]*20001
            cnt=0
            l=0
            n=len(nums)
            for r in range(n):
                x=nums[r]
                freq[x]+=1
                if freq[x]==1: dist+=1
                while dist>k:
                    y=nums[l]
                    freq[y]-=1
                    if freq[y]==0: dist-=1
                    l+=1
                cnt+=(r-l+1)
            return cnt
        
        if k==1: return goodLessEqualK(nums, k)
        else: return goodLessEqualK(nums, k)-goodLessEqualK(nums, k-1)