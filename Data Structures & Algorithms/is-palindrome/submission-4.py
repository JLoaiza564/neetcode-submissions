class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(map(lambda c: c.lower(), filter(lambda x: x.isalnum(), s)))

        print(s)

        return s == s[::-1]
        