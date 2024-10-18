class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def condition(mid, lo, hi):
            if nums[mid] == target:
                return "found"
            elif nums[mid] < target:
                if nums[lo] >= nums[mid] and target > nums[hi]:
                    return "left" 
                else:
                    return "right"
            else:
                if nums[mid] >= nums[lo] > target:
                    return "right"
                else:
                    return "left"

        def binary_search(lo, hi, condition):
            while lo <= hi:
                mid = (lo + hi) // 2
                result = condition(mid, lo, hi)
                print(result, mid, lo , hi)

                if result == "found":
                    return mid
                elif result == "left":
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        return binary_search(0, len(nums)-1, condition)
        
