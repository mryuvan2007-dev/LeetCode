class Solution(object):
    def lengthOfLongestSubstring(self, s):
        curr = ""
        leng = 0

        for ch in s:
            if ch in curr:
                curr = curr[curr.index(ch) + 1:]
            curr += ch
            leng = max(leng, len(curr))

        return leng
