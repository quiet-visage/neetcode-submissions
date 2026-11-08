class Solution:
    "([)]"
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False
        equiv = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = deque()
        for elem in s:
            is_closing = elem in equiv

            if is_closing:
                if not stack:
                    return False
                if stack[-1] != equiv[elem]: 
                    return False
                stack.pop()
                continue
            stack.append(elem)
        
        return len(stack) == 0
        