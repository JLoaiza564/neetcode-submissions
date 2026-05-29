class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        
        longest = 0

        for c in chars:
            
            r = l = 0
            diff_chars = 0
            while r < len(s):
                if s[r] != c:
                    diff_chars += 1

                curr_length = r - l + 1
                
                is_valid_substring = diff_chars <= k
                while not is_valid_substring:
                    if s[l] != c:
                        diff_chars -= 1
                    l += 1
                    is_valid_substring = diff_chars <= k
                
                longest = max(longest, r - l + 1)

                r += 1

        return longest