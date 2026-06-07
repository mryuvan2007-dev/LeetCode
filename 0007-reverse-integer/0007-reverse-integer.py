class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1 # check it is negative or positive ,if positive then store sign =-1
        #'-123' reverse= '321-' its wrong in sign back side so change to positive first.
        x=abs(x) # change negative to positive number  
        rev=int(str(x)[::-1]) # reverse it by making as a string 
        rev=rev*sign
        

         # Check 32-bit signed integer range
        if rev < -2**31 or rev > 2**31 - 1: # check from -32 bit to +32 bit numbers
            return 0 # if there return zero
        return rev


        