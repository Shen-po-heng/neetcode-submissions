class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store_sign={"(","{","["}

        for i in s:
            if i in store_sign:
                stack.append(i)
                continue

            if not stack:
                return False
                
            if ((i == ")" and stack[-1] == "(")
                or (i == "]" and stack[-1] == "[")
                or (i == "}" and stack[-1] == "{")
                ):
                stack.pop()
            else:
                return False
        return not stack