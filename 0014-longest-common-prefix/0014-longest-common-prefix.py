class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: # if no input was given  return empty 
            return ""
    
        strs.sort() #order the strings in ascending order
        first = strs[0] # consider the first string as first
        last = strs[-1] # consider the last string as last string
        
        i = 0 
        while i < len(first) and first[i] == last[i]: # compare the sting one by one stop it when you reach the end
            i += 1
        
        return first[:i] #return the common prefix of all the strings