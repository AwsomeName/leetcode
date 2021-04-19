class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return s
        if numRows == 1:
            return s
        res = [ [] for i in range(numRows) ]
        xxx = (numRows-1) * 2 
        for idx, nc in enumerate(s):
            x = idx % xxx
            if x > numRows - 1:
                x = numRows - x - 2
            res[x].append(nc)
            
        res_str = ""
        for i in res:
            res_str += "".join(i)
        return res_str
