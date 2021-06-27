class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen = len(s)
        plen = len(p)
        re_flag = [[False] * (plen+1) for x in range(slen+1)]
                                                                                    
        re_flag[0][0] = True

        for j in range(1, plen, 2):
            if p[j] == "*" and re_flag[0][j-1]:
                re_flag[0][j+1] = True
        # print re_flag
                                                            
        for i in range(slen):
            for j in range(plen):
                if s[i] == p[j] or p[j] == ".":
                    re_flag[i+1][j+1] = re_flag[i][j]
                elif p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".":
                        re_flag[i+1][j+1] = re_flag[i+1][j-1]
                    else:
                        re_flag[i+1][j+1] = re_flag[i+1][j-1]|re_flag[i+1][j]|re_flag[i][j+1]
                        # print i+1, j+1, re_flag[i+1][j+1]
        
        # print re_flag
        return re_flag[slen][plen]
