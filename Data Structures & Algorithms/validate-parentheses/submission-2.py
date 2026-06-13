class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        curr = s[0]
        opBrack = []
        for bracket in s:
            if bracket in ('(', '[', '{'):
                opBrack.append(bracket)
            else:
                if not opBrack:
                    return False
                curr = opBrack[-1]
                if curr == '(' and bracket != ')':
                    return False
                if curr == '[' and bracket != ']':
                    return False
                if curr == '{' and bracket != '}':
                    return False

                opBrack.pop()
                
        if not len(opBrack):
            return True

        return False
        