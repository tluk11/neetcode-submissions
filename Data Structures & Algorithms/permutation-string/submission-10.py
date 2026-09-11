class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 cannot be longer than s2
        if len(s1) > len(s2):
            return False
            
        dicts1 = defaultdict(int)
        for s in s1:
            dicts1[s] += 1

        # 'value' tracks how many unique characters are currently UNMATCHED
        value = len(dicts1)
        
        # 1. Initialize ONLY the first window of size len(s1)
        for i in range(len(s1)):
            s = s2[i]
            if s in dicts1:
                dicts1[s] -= 1
                if dicts1[s] == 0:
                    value -= 1      # We achieved a perfect match
                elif dicts1[s] == -1:
                    value += 1      # We added too many, breaking a previous match
                    
        if value == 0:
            return True
            
        # 2. Slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            # Remove left character
            temp1 = s2[l]
            if temp1 in dicts1:
                dicts1[temp1] += 1
                if dicts1[temp1] == 0:
                    value -= 1      # Removing excess fixed a match
                elif dicts1[temp1] == 1:
                    value += 1      # Removing broke a perfect match
            
            # Add right character
            temp2 = s2[r]
            if temp2 in dicts1:
                dicts1[temp2] -= 1
                if dicts1[temp2] == 0:
                    value -= 1      # Adding fixed a match
                elif dicts1[temp2] == -1:
                    value += 1      # Adding broke a match with excess
                    
            if value == 0:
                return True
                
            l += 1
            
        return False