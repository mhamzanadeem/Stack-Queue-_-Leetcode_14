class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        chars = list(s)

        for i, ch in enumerate(chars):
            if ch == "(":
                stack.append(i)

            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""

        # Any '(' left in stack is unmatched
        for i in stack:
            chars[i] = ""

        return "".join(chars)