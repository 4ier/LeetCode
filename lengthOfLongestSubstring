def main():
    sln = Solution()
    strs = ["au", "wpwkew", "bbbbbb", "abcabcbb", "dvdf"]
    for st in strs:
        sln.lengthOfLongestSubstring(st)
        print "--------"


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        past = {}
        result = start = 0
        for a, ch in enumerate(s):
            if ch in past and start <= past[ch]:
                start = past[ch] + 1
            else:
                result = max(result, a - start + 1)
            past[ch] = a
            print past
            print start
        print 'result: ', result
        return result

if __name__ == "__main__":
    main()
