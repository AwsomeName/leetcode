class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        n_f = False
        if x < 0:
            n_f = True
            x = -x
        
        res = 0
        while x > 0:
            tmp = x % 10
            if not n_f and res * 10 + tmp < 2147483647:
                res = res * 10 + tmp
            elif n_f and res * 10 + tmp < 2147483648:
                res = res * 10 + tmp
            else:
                return 0
            x = x / 10
        if n_f:
            return -res
        else:
            return res

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        Output = ''
    
        if x == 0:
            Output = 0
            return(Output)

        Zahl = x

        Stop = 0
        while Stop == 0:
            if Zahl%10 == 0:
                Zahl = Zahl/10
            else:
                Stop = 1

        Zahl_str = str(int(abs(Zahl)))

        #print(Zahl_str)


        for i in range(1,len(Zahl_str)+1):
            Output = Output + (Zahl_str[i*-1])

        Output = int(Output)

        if Output > 2**31 - 1 or Output < (-2)**31:
            return(0)


        if Zahl < 0:
            Output *= (-1)
        return(Output)
