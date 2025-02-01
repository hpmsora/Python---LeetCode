class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(k):
            mp[nums[i]] +=1

        distinct = len(mp)
        res = [distinct]

        l = 0
        for r in range(k, len(nums)):
            if mp[nums[r]] == 0:
                distinct+=1
            mp[nums[r]] +=1

            if mp[nums[l]] ==1:
                distinct -=1
            mp[nums[l]] -=1
            l+=1
            res.append(distinct)
        return res