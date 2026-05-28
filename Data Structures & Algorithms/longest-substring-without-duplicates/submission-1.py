class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                chars.add(s[j])
                longest = max(longest, len(chars))

        return longest