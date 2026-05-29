class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        longest = 0
        count_most_frequent = 0
        most_frequent = None


        l = 0
        for r in range(len(s)):
            if s[r] not in counts:
                counts[s[r]] = 0
            counts[s[r]] += 1

            if counts[s[r]] > count_most_frequent:
                count_most_frequent = counts[s[r]]


            len_curr_substring = r - l + 1
            is_valid_substring = len_curr_substring - count_most_frequent <= k

            while not is_valid_substring:
                counts[s[l]] -= 1
                l += 1
                len_curr_substring = r - l + 1
                is_valid_substring = len_curr_substring - count_most_frequent <= k

            longest = max(longest, len_curr_substring)




        return longest