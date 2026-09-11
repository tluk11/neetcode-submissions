class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = Counter(t)
        have = defaultdict(int)

        right,left = 0,0
        minlen = float('inf')
        res = ""
        have_count = 0
        while right < len(s):
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    have_count+=1
            while have_count == len(need):
                if right - left + 1 < minlen:
                    minlen = right -left +1 
                    res = s[left:right+1]
                if s[left] in have:
                    have[s[left]] -= 1
                    if have[s[left]] < need[s[left]]:
                        have_count -= 1
                left+=1
            right += 1
        return res 