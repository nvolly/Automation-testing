class Solution(object):
    def twoSum(self, nums, target):
        seen_indices = {}
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_indices:
                return [seen_indices[complement], i]
            seen_indices[num] = i
        return None

print("two_sum.py: ", __name__)