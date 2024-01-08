class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_left = 0
        index_right = len(numbers) - 1

        while index_left < index_right:
            left = numbers[index_left]
            right = numbers[index_right]

            left_right = left + right
            if left_right == target:
                return [index_left + 1, index_right + 1]
            elif left_right > target:
                index_right -= 1
            else:
                index_left += 1