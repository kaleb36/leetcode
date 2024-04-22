class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new = []
        
        for x in nums:
            if x != val:
                new.append(x)
        
        for i in range(len(new)):
            nums[i] = new[i]
        k = len(new)
        return k
