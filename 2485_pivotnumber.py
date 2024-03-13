class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        for pivot in range(1, n+1):
            _1tox = sum(i for i in range(1, pivot+1))
            _xton = sum(j for j in range(pivot, n+1))
            if _1tox == _xton:
                return pivot

        return -1
