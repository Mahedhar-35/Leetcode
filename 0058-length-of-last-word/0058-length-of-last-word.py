class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=list(s)
        print(st)
        st=st[::-1]
        i=0
        n = len(st)
        
        while i < n and st[i] == ' ':
            i += 1
        count = 0
        while i < n and st[i] != ' ':
            count += 1
            i += 1
            
        return count