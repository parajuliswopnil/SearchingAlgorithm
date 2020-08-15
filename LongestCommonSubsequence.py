def longestCommonSubsequence(A, B, m, n, memotize):
    if (m == 0 or n == 0):
        return 0

    elif (memotize[m - 1][n - 1] != -1):
        return memotize[m - 1][n - 1]

    elif (A[m - 1] == B[n - 1]):
        memotize[m - 1][n - 1] = 1 + longestCommonSubsequence(A, B, m - 1, n - 1, memotize)
        return memotize[m - 1][n - 1]

    else:
        memotize[m - 1][n - 1] = max(longestCommonSubsequence(A, B, m, n - 1, memotize),
                                     longestCommonSubsequence(A, B, m - 1, n, memotize))
        return memotize[m - 1][n - 1]


A = "copyrightable"
B = "copyright"
m = len(A)
n = len(B)

memotize = [[-1 for i in range(n + 1)]
            for i in range(m + 1)]

print("Length of longest common subsequence is: "+str(longestCommonSubsequence(A, B, m, n, memotize)))
