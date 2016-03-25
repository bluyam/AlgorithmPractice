def prettyPrint(A):
    answer =[[1]]
    for i in range(2,A+1):
        for j in answer:
            j.insert(0,i)
            j.append(i)
        row_length = (i*2)-1
        answer.insert(0,[i]*(row_length))
        answer.append([i]*(row_length))
    return answer

print prettyPrint(3)