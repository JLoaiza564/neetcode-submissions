from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)

        
        answer = ""

        for i in range(len(s)):
            curr_counts = Counter()
            for j in range(i, len(s)):
                curr_counts.update([s[j]])
                are_counters_equal = True
                for char in t_counts:
                    if t_counts[char] > curr_counts[char]:
                        are_counters_equal = False

                if are_counters_equal:
                    if answer == "" or j - i + 1 < len(answer):
                        answer = s[i:j+1]
        
        return answer