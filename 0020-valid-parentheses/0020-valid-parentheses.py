class Solution(object):
    def isValid(self, s):
        stack = []
        symbol= {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in symbol.values():     
                stack.append(ch)
            else:                         
                if not stack or stack.pop() != symbol[ch]:
                    return False

        return not stack
