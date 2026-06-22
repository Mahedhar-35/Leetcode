class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text=list(text)
        D={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i=="b" or i=="a" or i=="n":
                D[i]+=1
            elif i=="l" or i=="o":
                D[i]+=0.5
        m=min(D.values())
        return int(m)