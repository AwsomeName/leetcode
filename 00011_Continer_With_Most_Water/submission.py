class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x, y = 0, len(height) - 1
        max_w = 0
                                                                    
        while x < y:
            width = y - x 
            high = min(height[x], height[y])
            max_w = max(width * high, max_w)
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
        
        return max_w
