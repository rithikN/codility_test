def solution(N, A):
    # Implement your solution here
    new_list = [0] * N
    max_val = 0
    for no in A:
        if no > N:
            new_list = [max_val] * N
            continue
        new_list[no -1] = new_list[no -1] + 1
        if max_val < new_list[no -1]:
            max_val = new_list[no -1]
    return new_list
