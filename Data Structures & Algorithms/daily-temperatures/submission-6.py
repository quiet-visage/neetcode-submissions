from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = deque()

        for i in reversed(range(n)):
            cur_temp = temperatures[i]

            if not stack:
                stack.append((i, cur_temp))
                continue
            
            top_id, top_temp = stack[-1]
            while stack and top_temp <= cur_temp:
                stack.pop()
                if stack:
                    top_id, top_temp = stack[-1]
            
            if top_temp < cur_temp:
                stack.append((i, cur_temp))
                continue
            
            stack.append((i, cur_temp))
            if top_temp != cur_temp:
                result[i] = top_id - i

        return result
        