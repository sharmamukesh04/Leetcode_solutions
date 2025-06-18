class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if len(stack)>0:
                last = stack[-1]
                if (last=='(' and ch==')') or (last == '{' and ch == '}') or (last == '[' and ch == ']'):
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        return len(stack)==0
        