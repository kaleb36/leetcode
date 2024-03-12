class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        case = True
        num = 1
        count = 0

        while case:
            if num not in arr:
                count += 1
                if count == k:
                    return num
                    case = False
            num += 1

