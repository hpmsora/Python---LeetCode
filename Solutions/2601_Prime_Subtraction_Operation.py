class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # 1. find prime number list
        primes_list = []
        for each_nums in range(2, 1001):
            isPrime = True
            for less_num in range(2, each_nums):
                if each_nums % less_num == 0:
                    isPrime = False
                    break
            if isPrime:
                primes_list.append(each_nums)
        
        # 2. Make each number to smallest possible number
        prev_num = 0
        index = 0
        while index < len(nums):
            value = nums[index]
            diff = value - prev_num

            max_sub = 0
            for each_primes in primes_list:
                if each_primes < diff:
                    max_sub = each_primes

            nums[index] = value - max_sub

            if nums[index] <= prev_num:
                return False
            prev_num = nums[index]
            index += 1
        return True