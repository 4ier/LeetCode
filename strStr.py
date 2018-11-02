class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if haystack == needle:
            return 0

        for i in range(len(haystack)):
            subStr = ''.join(haystack[i : i + len(needle)])
            if len(needle) > len(subStr):
                return -1

            if subStr == needle:
                return i
        return  -1


def main():
    sln = Solution()
    print sln.strStr('abcc', 'cc')

if __name__ == '__main__':
    main()
