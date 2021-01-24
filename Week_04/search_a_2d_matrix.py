class Solution:
  def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]: return False
    n_col = len(matrix[0])
    # use a 1-D index as if the matrix is flattend
    start, end = 0, len(matrix) * n_col - 1
    while start <= end:
      # avoid overflow of start + end
      mid = start + (end - start) // 2
      # get the corresponding value in 2d matrix
      val_mid = matrix[mid // n_col][mid % n_col]
      # normal binary search from here
      if val_mid == target: return True
      if target > val_mid:
        start = mid + 1
      else:
        end = mid - 1
    return False
