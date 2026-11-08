class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        m_pair = [0,0]
        m_vol = 0

        while left != right:
            width = right - left
            height = min(heights[right], heights[left])
            vol = width * height
            if vol > m_vol:
                m_pair = [left,right]
                m_vol = vol
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left +=1
        
        return m_vol

