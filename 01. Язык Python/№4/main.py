def cumsum_and_erase(A, erase = 1):
    N = len(A)
    B = [0] * N
    B[0] = A[0]
    for i in range(0, N):
            B[i] = B[i - 1] + A[i]
    C = list(filter(lambda x: x != erase, B))
    return C
