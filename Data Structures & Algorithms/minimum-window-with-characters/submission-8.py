from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)

        answer = ""

        curr_counts = Counter()
        i = 0
        for j in range(len(s)):
            curr_counts.update([s[j]])

            is_valid_substring = True
            for char in t_counts:
                if t_counts[char] > curr_counts[char]:
                    is_valid_substring = False
            
            if is_valid_substring:

                while t_counts[s[i]] < curr_counts[s[i]]:
                    curr_counts[s[i]] -= 1
                    i += 1
                

                if answer == "" or len(answer) > j - i + 1:
                    answer = s[i:j+1]
        
        return answer