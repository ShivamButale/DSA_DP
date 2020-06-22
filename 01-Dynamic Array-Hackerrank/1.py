def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    sequence = [[] for i in range(n)]
    result = []
    for q in queries:
        if q[0] == 1:
            curr_result = (q[1] ^ last_answer) % n
            sequence[curr_result].append(q[2])
        else:
            curr_seq = (q[1] ^ last_answer) % n
            size = len(sequence[curr_seq])
            temp = q[2] % size
            last_answer = sequence[curr_seq][temp]
            result.append(last_answer)
    return result
