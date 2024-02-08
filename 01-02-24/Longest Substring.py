'''Given a string s, find the length of the longest 
substring
 without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

PROGRAM CODE:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a,y,x= 0,0,0
        t = {}
        b = len(s)
        while(x < b):
            c = s[x]               
            t[c] = 1 if not c in t else t[c] + 1                      
            if t[c] > 1:
                while(t[c] > 1):
                    t[s[y]] =t[s[y]]- 1
                    y=y+1                    
            a = max(a,x-y+1)
            x=x+1
        return a
