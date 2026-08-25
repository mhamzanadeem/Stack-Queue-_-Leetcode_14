class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def checkbackspace(strings):
            stack = []

            for char in strings:
                if char == "#":
                     if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return checkbackspace(s) ==  checkbackspace(t)