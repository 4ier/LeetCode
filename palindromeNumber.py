class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        tmp = 0
        while x > tmp:
            tmp = 10 * tmp + (x % 10)
            # print("tmp" + str(tmp))
            x = x / 10
            # print("x" + str(x))
        return (x == tmp or x == tmp / 10)


def main():
    sln = Solution()
    # print(sln.isPalindrome(0))
    print(sln.isPalindrome(10))
    # print(sln.isPalindrome(9876789))
    # print(sln.isPalindrome(98766))


if __name__ == '__main__':
    main()
