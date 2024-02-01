class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_list = nums[:]
        for i in range(len(nums)):
            print(new_list.index(new_list[i]))
            new_list.pop(new_list.index(nums[i]))
            for j in new_list:
                _sum = nums[i] + j

                if _sum == target:
                    print(nums)
                    return i, nums.index(j, i+1)
                    break


a =[3,2,4] #[2, 7,11,15]#[2, 5, 5, 11]
target = 6
kk = Solution()
b = list(kk.twoSum(a, target))
print(b)
