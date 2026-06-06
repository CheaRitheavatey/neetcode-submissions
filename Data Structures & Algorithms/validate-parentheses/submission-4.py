class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in dic:
                stack.append(i)

            elif  not stack or i != dic[stack.pop()] :
                return False
       
        return not stack

        # s=  "([{}])"
        # for i in s:
        # if i is (, [, { -> we push into stack
        # if ), },] -> we pop but 
        # if the stack is empty -> true else false
