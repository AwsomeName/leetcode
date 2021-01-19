class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        tail = 0
        n_tail = 0
        max_len = 1
        queue = {}
        for idx, v in enumerate(s):
            if v in queue:
                n_tail = queue[v] + 1
                # 删除队列tail到idx的value
                for k in range(tail, n_tail):
                    queue.pop(s[k])
            tail = n_tail
            if max_len < idx - tail + 1:
                max_len = idx - tail + 1
            queue[v] = idx
        return max_len