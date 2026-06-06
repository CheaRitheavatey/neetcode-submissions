class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1 2 + 3 * 4 -
        # when we see number -> we push [1 2 ]
        # when we see operand -> we pop until empty + 
        # 2 + 1 = 3 -> result push back
        # [3 3]
        # 3 * 3 = 9
        # [9 4]
        # 9 - 4

        stack = []
        result = 0
        operand = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operand:
                print("push tokens[i]", i)
                stack.append(int(i))
                print(stack)
            else:
                a = stack.pop()
                print(a)
                b = stack.pop()
                print(b)
                if i == operand[0]:
                    stack.append(a + b)
                elif i == operand[1]:
                    stack.append(b-a)
                elif i == operand[2]:
                    stack.append(b*a)
                elif i == operand[3]:
                    stack.append(int(b/a))
        return stack[0]
            

        