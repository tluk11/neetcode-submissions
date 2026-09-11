class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left,right = 0,len(s1)-1
        s1count,s2count = [0]*26,[0]*26
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1

        while right < len(s2):
            
            if s1count == s2count:
                return True
            s2count[ord(s2[left])-ord('a')]-=1
            left+=1
            right+=1
            if right < len(s2):
                s2count[ord(s2[right])-ord('a')]+=1
        return False 