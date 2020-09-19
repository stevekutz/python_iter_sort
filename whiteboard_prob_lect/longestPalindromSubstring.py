"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''        
        def is_pal(x):
            return x == x[::-1]        
        window_size = len(s)        
        
        while window_size > 1:
            for i in range(len(s) - window_size + 1): 
                substring = s[i : i + window_size]
                if is_pal(substring):
                    return substring
            window_size -= 1   
            
        return s[0]