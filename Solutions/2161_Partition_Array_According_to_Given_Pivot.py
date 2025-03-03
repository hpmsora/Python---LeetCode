class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []

        for each_nums in nums:
            if each_nums < pivot:
                left.append(each_nums)
            elif each_nums > pivot:
                right.append(each_nums)
            else:
                mid.append(each_nums)
        
        return left + mid + right