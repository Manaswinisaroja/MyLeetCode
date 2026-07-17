 """
  Problem: 283. Move Zeroes
  Difficulty: Easy
  Pattern: Two Pointers
  Time Complexity: O(n)
  Space Complexity: O(1)
  """
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

'''
Brute Force Approach
class Solution(object):
    def moveZeroes(self, nums):
        arr = []
        cnt = 0
        for i in nums:
            if i != 0:
                arr.append(i)
            else:
                cnt += 1
        for i in range(cnt):
            arr.append(0)
        nums[:] = arr
'''
