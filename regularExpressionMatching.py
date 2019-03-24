class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p.__contains__('*'):
            return True
        else:
            index = 0
            for i in range(len(s)):
                j = i
                index = i
                while j < len(p) - 1 and (s[i] != p[j] or p[j] != '.'):
                    j = j + 1
                if j == len(p):
                    break
            return index == len(s) - 1