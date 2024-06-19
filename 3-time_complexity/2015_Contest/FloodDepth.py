# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Find the maximum depth of water in mountains after a huge rainfall.

def solution(A):
  # Implement your solution here

  '''
  Task Score: 66%
  Correctness: 100%
  Performance:  33%
  Detected time complexity: O(N**2)
  '''
  lenA = len(A)
  maxDepth = 0
  for i, no in enumerate(A[1:-1]):
      i += 1
      l = r = i
      if A[i] <= A[i - 1] and A[i] <= A[i + 1]:
          lmax = A[i - 1]
          rmax = A[i + 1]
          while l  > 0 or r < (lenA-1):
              if l > 0:
                  l -= 1
              if r < (lenA -1):
                  r += 1
              if A[i] == A[l] or  A[i] == A[r]:
                  continue
              lmax = max(lmax, A[l])
              rmax = max(rmax, A[r])
          minPeak = min(lmax, rmax)
          depth = minPeak - A[i]
          maxDepth = max(maxDepth, depth)

  return maxDepth 



