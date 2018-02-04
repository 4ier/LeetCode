class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        length = 2 * (numRows - 1)
        result = [""] * numRows
        row = 0
        col = 0
        rem = 0
        div = 0
        for index, c in enumerate(s):
            rem = index % length
            div = index / length
            if rem < numRows:
                row = rem
                col = div * (numRows - 1)
            else:
                row = length - rem
                col = (div + 1) * (numRows - 1) - row

            print("row: " + str(row))
            print("col: " + str(col))
            print("====char: " + str(c))
            result[row] += c

        return "".join(result)


def main():
    sln = Solution()
    print(sln.convert("abcdef", 3))


if __name__ == '__main__':
    main()
