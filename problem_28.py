#find the index of the first occurence in a string

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack.startswith(needle):
            return haystack.index(needle[0])
        elif haystack.find(needle) != -1:
            return haystack.find(needle)

        return -1
