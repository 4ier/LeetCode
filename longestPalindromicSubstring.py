class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmpS = ""
        for i in range(len(s)):
            offset = 0
            iLeft = i
            iRight = i
            while iLeft - offset >= 0 \
                    and iRight + offset < len(s):
                if s[iLeft - offset] == s[iRight + offset]:
                    offset += 1
                else:
                    break
            if len(tmpS) < len(s[iLeft - offset + 1:iRight + offset]):
                tmpS = s[iLeft - offset + 1:iRight + offset]
                offset = 0


        for i in range(len(s)):
            offset = 0
            iLeft = i
            iRight = i + 1
            while iLeft - offset >= 0 \
                    and iRight + offset < len(s):
                if s[iLeft] != s[iRight]:
                    break
                else:
                    if s[iLeft - offset] == s[iRight + offset]:
                        offset += 1
                    else:
                        break
            if len(tmpS) < len(s[iLeft - offset + 1:iRight + offset]):
                tmpS = s[iLeft - offset + 1:iRight + offset]
                offset = 0

        return tmpS


if __name__ == '__main__':
    sln = Solution()
    print (sln.longestPalindrome("babad"))
