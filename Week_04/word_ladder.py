import string

class Solution:
  def ladderLength(self, beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
      return 0
    front = set([beginWord])
    back = set([endWord])
    length = 2
    while front:
      new_words = set([])
      # find all words in wordList that can transform from words in front
      front = words & set([w[:i] + c + w[i + 1:] for w in front for i in range(len(w)) for c in string.ascii_lowercase])
      # any word in front can transform to any word in back
      if front & back:
        return length
      # count length
      length += 1
      # choose the end with less banches for next iteration
      if len(front) > len(back):
        front, back = back, front
      # remove used words from wordList to avoid loops
      words -= front
    return 0
