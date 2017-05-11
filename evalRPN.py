class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for ele in tokens:
            try:
                int(ele)
            except ValueError:
                right = int(stack.pop())
                left = int(stack.pop())
                if left * right < 0 and left % right != 0 and ele == '/':
                    value = eval(str(left) + str(ele) + str(right)) + 1
                else:
                    value = eval(str(left) + str(ele) + str(right))
                stack.append(value)
            else:
                stack.append(ele)

        return int(stack[0])


def main():
    sln = Solution()

    ipt = [["2", "1", "+", "3", "*"],
           ["4", "13", "1", "/", "+"], ["3", "-4", "+"], ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
    for arr in ipt:
        print sln.evalRPN(arr)

if __name__ == '__main__':
    main()
