class Solution:
    def romanToInt(self, s):
        """
        :type num: int
        :rtype: str
        """
        charValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        result = charValue[s[len(s) - 1]]
        for i in range(len(s) - 2, 0, -1):
            if s[i] < s[i + 1]:
                result = result - charValue[s[i]]
            else:
                result = result + charValue[s[i]]
        return result
