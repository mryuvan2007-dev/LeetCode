class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)
       #Index: 0 1 2 3 4 5 6 7 8   
          #dp:    T F F F F F F F F    #by default index 0 must be true (to ensure its empty string condition)
        

         #loopoing the given string s
        for i in range(1, len(s) + 1):
            for word in wordDict: #store each worddict in 'word'
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word: #checking its availability
                    dp[i] = True # if there return true

        return dp[-1] 



        