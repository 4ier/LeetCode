class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = 0
        while x > tmp:
            tmp = 10 * tmp + (x % 10)
            x = x / 10
        return (x == tmp or x == tmp / 10)

