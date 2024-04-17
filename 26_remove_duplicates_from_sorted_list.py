class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        norep_nums = list(set(nums))
        norep_nums.sort()
        
        k = len(norep_nums)
        for i in range(k):
            nums[i] = norep_nums[i]

        return k
