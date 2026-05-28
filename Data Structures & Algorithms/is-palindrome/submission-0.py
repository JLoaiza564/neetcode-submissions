class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(list(filter(lambda x: x.isalnum(), s)))

        for i in range(len(s)):
            if s[i].lower() != s[-(i+1)].lower():
                print(s[i], s[-(i+1)])
                return False

        
        return True
        