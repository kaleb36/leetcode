#Divide array into arrays with max difference
#You are given an integer array nums of size n and a positive integer k.
#Divide the array into one or more arrays of size 3 satisfying the following conditions:
#Each element of nums should be in exactly one array.
#The difference between any two elements in one array is less than or equal to k.
#Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

#________begin of code________

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        count = [x+1 for x in range(len(nums))]
        new_list = []

        for i in count:
            if i % 3 == 0:
                _diff = nums[i-1] - nums[i-3]
                if 0 <= _diff <= k:
                    new_list += [[nums[i-3], nums[i-2], nums[i-1]]]
                else:
                    return []
        return new_list

nums_list = [1,3,4,8,7,9,3,5,1]
_k = 3

soln = Solution()
print(soln.divideArray(nums_list, _k))
