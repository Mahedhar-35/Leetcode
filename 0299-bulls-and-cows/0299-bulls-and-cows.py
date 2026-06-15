class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s=list(str(secret))
        g=list(str(guess))
        result=[]
        a=0
        b=0
        counts = [0] * 10
        
        for i in range(len(g)):
            s_digit = int(s[i])
            g_digit = int(g[i])
            
            if g[i] == s[i]:
                a += 1
            else:
                if counts[s_digit] < 0:
                    b += 1
                if counts[g_digit] > 0:
                    b += 1
                counts[s_digit] += 1
                counts[g_digit] -= 1
                
        result.append(str(a))
        result.append("A")
        result.append(str(b))
        result.append("B")            
        return "".join(result)
