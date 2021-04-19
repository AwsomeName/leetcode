class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        queue = {}
        start = 0
        
        for idx, ns in enumerate(s):
            if ns in queue and start <= queue[ns]:
                start = queue[ns] + 1
            
            queue[ns] = idx
            max_length = max(idx - start + 1, max_length)
                
        return max_length
