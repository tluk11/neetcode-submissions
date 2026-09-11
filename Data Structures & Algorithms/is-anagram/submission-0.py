class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter 
        Scount = Counter(s)    
        Tcount = Counter(t)

        return Scount == Tcount