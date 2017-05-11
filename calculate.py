# '''
# Keep a global running total and a stack of signs (+1 or -1), one for each open scope. The "global" outermost sign is +1.

# Each number consumes a sign.
# Each + and - causes a new sign.
# Each ( duplicates the current sign so it can be used for the first term inside the new scope. That's also why I start with [1, 1] - the global sign 1 and a duplicate to be used for the first term, since expressions start like 3... or (..., not like +3... or +(....
# Each ) closes the current scope and thus drops the current sign.
# Also see the example trace below my programs.
# '''
class Solution(object):
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total


def main():
    sln = Solution()

    #ipt = [["1 + 1", 2], [" 2-1 + 2 ", 3], ["(1+(4+5+2)-3)+(6+8)", 23]]
    ipt = [["(1+(4+5+2)-3)+(6+8)", 23]]
    for arr, result in ipt:
        value = int(sln.calculate(arr))
        if result == value:
            print 'passed'
        else:
            print 'failed'

if __name__ == '__main__':
    main()
