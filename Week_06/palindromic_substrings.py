class Solution:
  def countSubstrings(self, s):
    def count(s, start, end):
      """
      Count # of palindromic strings whose center is s[start:end+1]
      """
      res = 0
      while start >= 0 and end < len(s):
        # not a palindomic
        if s[start] != s[end]: break
        # count and expand
        res += 1
        start -= 1
        end += 1
      return res

    result = 0
    for i in range(len(s)):
      # count for 1-char and 2-char centers, sum up
      result += count(s, i, i) + count(s, i, i + 1)
    return result


if __name__ == "__main__":
  print(Solution.countSubstrings(None, "abc"))
  print(Solution.countSubstrings(None, "aaa"))
