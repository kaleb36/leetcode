class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ind = 0
        int_num = 0
        num2 = 0

        while ind <= len(s)-1:
            num1 = num_dict[s[ind]]
            if ind < len(s) - 1:
                num2 = num_dict[s[ind+1]]

            if num1 < num2:
                int_num = (num2 - num1) + int_num
                ind += 2
                num2 = 0

            else:
                int_num += num1
                ind += 1
        return int_num 
        
