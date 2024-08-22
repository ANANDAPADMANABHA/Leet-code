class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for char in s:
            if char == '(':
                if stack:
                    result.append(char)
                stack.append(char)
            elif char == ')':
                stack.pop()
                if stack:
                    result.append(char)

        return "".join(result)



