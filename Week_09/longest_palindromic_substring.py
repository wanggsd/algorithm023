class Solution:
  def longestPalindrome(self, s):
    def expand(s, start, end):
      """
      Find longest palindrome centering at s[start:end + 1]
      """
      while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
      return s[start + 1: end]

    res = ""
    for i in range(len(s)):
      # find the longest palindrome centering at s[i]
      cur = expand(s, i, i)
      if len(cur) > len(res):
        res = cur

      # find the longest palindrome centering at s[i:i+2]
      cur = expand(s, i, i + 1)
      if len(cur) > len(res):
        res = cur
    return res


if __name__ == "__main__":
  assert Solution.longestPalindrome(None, "babad") == "bab"
  assert Solution.longestPalindrome(None, "cbbd") == "bb"
  assert Solution.longestPalindrome(None, "a") == "a"
  assert Solution.longestPalindrome(None, "ac") == "a"
