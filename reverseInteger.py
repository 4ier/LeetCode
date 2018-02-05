class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        op = ""
        xStr = str(x)
        result = ""
        if x < 0:
            xStr = str(0 - x)
            op = "-"
        for i in range(len(xStr)):
            result += xStr[len(xStr) - i - 1]
        ret = int(op + result)
        if ret > 2 ** 31 - 1 or ret < -2**31:
            return 0
        else:
            return ret


def main():
    sln = Solution()
    print(sln.reverse(-120))


if __name__ == '__main__':
    main()
