class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest_length = 0

        for i in range(len(s)):
            counts = {}
            num_most_frequent = 0
            for j in range(i, len(s)):
                if s[j] not in counts:
                    counts[s[j]] = 0

                counts[s[j]] += 1

                num_most_frequent = max(num_most_frequent, counts[s[j]])

                curr_len = j - i + 1

                is_valid_substring = curr_len - num_most_frequent <= k

                if is_valid_substring:
                    longest_length = max(longest_length, curr_len)
                else:
                    break


        return longest_length
        