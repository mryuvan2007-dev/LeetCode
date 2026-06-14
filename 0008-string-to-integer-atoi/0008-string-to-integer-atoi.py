class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  #strip() removes spaces from both ends of the string.
        if not s:
            return 0  # when  sting is empty, return 0.
        i = 0 #i → current index in the string.
        sign = 1 #sign → stores whether the number is positive or negative.
                    #1 → positive
                    #-1 → negative
        result = 0 # stores the final value
        if s[i] == '-' or s[i] == '+': 
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1
        return sign * result