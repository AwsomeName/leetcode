# 这道题最离谱的是，用反转对照的方式会更快，

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        strlen = len(s)
        maxS = 0
        maxE = 0
        maxL = 0
        
        dp = [[False] * strlen for row in range(strlen)]
        
        for r in range(1, strlen):
            for l in range(0, r):
                if s[r] == s[l] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if (r - l + 1) > maxL:
                        maxL = r - l + 1
                        maxS = l
                        maxE = r
                        
                    
        return s[maxS: maxE+1]

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
