class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        sortedStrs = sorted(strs,key=len)
        shortest = sortedStrs[0]

        if len(shortest) == 0:
            return ""

        for i, char in enumerate(shortest):
            for other in sortedStrs[1:]:
                if other[i] != char:
                    return shortest[:i]
        return shortest

def main():
    sln = Solution()
    ipt = [[["ca","a"], ""],[["a","b"], ""],[["aaa","aac"], "aa"],[["asdfgdsa","asdcgdsa"], "asd"]]
    for arr, result in ipt:
        print('-----')
        print(arr)
        value = sln.longestCommonPrefix(arr)
        print(value)
        if result == value:
            print('passed')
        else:
            print('failed')

if __name__ == '__main__':
    main()