class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(s.split())
        beg,end = 0,len(st)-1
        st = st.lower()
        while beg<end:
            while beg < end and not st[beg].isalnum():
                beg+=1
            while beg < end and not st[end].isalnum():
                end-=1
            if st[beg] == st[end]:
                beg+=1
                end-=1
            else:
                return False
        return True