class Solution(object):
     def isPalindrome(self, x):
         """
         :type x: int
         :rtype: bool
         """
         if x < 0:
             return False
                                                                        
         a = x
         b = 0
         while a > 0:
             b = b *10 + a % 10
             a = a / 10
             
         if b == x:
             return True
         else:
             return False
