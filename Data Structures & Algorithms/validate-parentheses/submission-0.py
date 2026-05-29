class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
            
            if not stack:
                return False

            if c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            if c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False


        return len(stack) == 0
        