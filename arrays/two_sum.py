from typing import List
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# 🤔 Naive (Brute Force) Approach
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             return [i, j]

      # Time Complexity: O(n²) → Nested loops
      # Space Complexity: O(1)

# class Solution:
# def twoSum(self, nums: List[int], target: int):
def twoSum(nums: List[int], target: int) -> List[int]:
    # -> List[int]
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
# nums = [2,7,11,15], target = 9
# sol = Solution()
print(twoSum([2,7,11,15], 9))