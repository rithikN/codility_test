# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    total_sum = sum(A)
    min_diff = float('inf')
    l_sum = 0

    for i in range(1,len(A)):
        l_sum += A[i-1]
        r_sum = total_sum - l_sum
        diff = abs(l_sum - r_sum)
        min_diff = min(diff, min_diff )

    return min_diff 
