class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # process space
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        if not s:
            return 0
        
        pf = False
        # process flag
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                pf = True
            s = s[1:]
            
        if not s:
            return 0
        
        # process 
        tmp = 0
        while len(s) > 0 and s[0] >= '0' and s[0] <= '9':
            tmp = tmp * 10 + int(s[0])
            # print tmp, s[0]
            s = s[1:]
            
        if pf:
            if -tmp < -2**31:
                return -2**31
            else:
                return -tmp
        else:
            if tmp > 2**31-1:
                return 2**31-1
            else:
                return tmp



class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        for i, c in enumerate(s):
            if c!=' ':
                break
        if i == len(s):
            return 0
        start_pos = i
        posflag = 1
        if s[i] == '-':
            posflag = -1
            start_pos = i+1
        elif s[i] == '+':
            start_pos = i+1
        end_pos = len(s)
        for i in range(start_pos, len(s)):
            if (s[i] < '0' or s[i] > '9'):
                end_pos = i
                break
        if start_pos == end_pos:
            return 0
        try:
            result = posflag*int(s[start_pos:end_pos])
        except:
            return 0
        if result <= -2**31:
            result = -2**31
        elif result >= 2**31:
            result = 2**31 - 1
        return result
