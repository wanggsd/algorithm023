class Solution:
  def numDecodings(self, s):
    if not s or s[0] == "0":
      return 0
    # res[i]: # of decodings of s[:i]
    res = [0 for _ in range(len(s) + 1)]
    res[:2] = 1, 1
    for i in range(2, len(s) + 1):
      if int(s[i - 1]) > 0:
        # decode s[i - 1] as one letter,
        # append to all decodings of s[: i - 2]
        res[i] = res[i  - 1]
      if 10 <= int(s[i - 2: i]) <= 26:
        # dcode s[i-2: i] as one letter,
        # append to all decodings of s[: i - 3]
        res[i] += res[i - 2]
    return res[-1]

if __name__ == "__main__":
  print(Solution.numDecodings(None, "12"))
  print(Solution.numDecodings(None, "226"))
  print(Solution.numDecodings(None, "0"))
  print(Solution.numDecodings(None, "06"))
