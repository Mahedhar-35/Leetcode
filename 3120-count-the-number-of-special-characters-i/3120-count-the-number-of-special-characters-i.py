class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        st=[word]
        s=set(word)
        s=list(s)
        small=[x for x in s if 'a' <= x <= 'z']
        cap=[x.lower() for x in s if 'A' <= x <= 'Z']
        count=0
        for i in small:
            if i in cap:
                count+=1
        return count        