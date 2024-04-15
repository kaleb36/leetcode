class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = strs[0]
        common = ""
        prev = -1
        for string in strs:
            if len(string) < len(shortest):
                shortest = string

        for strng in strs:
            for i in range(len(shortest)):
                if strng[i] == shortest[i] and i - prev == 1:
                    common += shortest[i]
                    prev = i

            if common == "":
                return ""
            shortest = common
            common = ""
            prev = -1
        return shortest
