class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        for i in s:
            if not stack:
                if i == '(':
                    stack.append(i)

                else:
                    stack.pop()
            else:
                if i == '(':
                    stack.append(i)
                    
                else:
                    stack.pop()
                    
                if  stack:

                    ans+=i

        return ans



