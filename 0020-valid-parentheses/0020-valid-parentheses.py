class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            
            if not stack:
                if i in dict:
                    return False
                else:
                    stack.append(i)
            
            else: 
                if i not in dict:
                    stack.append(i)
                    continue
                if dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        if not stack:
            return True
        return False