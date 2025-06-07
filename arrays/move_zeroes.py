# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Input:  nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Input: nums = [0]
# Output: [0]


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        print(nums)
        # Step 2: Fill the rest with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        print(nums)


sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
# nums = [-1, 3, -2, 4, 0]
# Transform it to: [3, 4, 0, -1, -2]  (non-negatives first, same order)

# insert_pos = 0

# def nonNegative(nums: List[int]):
#     insert_pos = 0
#     for i in range(len(nums)):
#         if nums[i] >= 0:
#             nums[insert_pos] = nums[i]
#             insert_pos += 1
        
#     print(nums)

# print(nonNegative(nums))