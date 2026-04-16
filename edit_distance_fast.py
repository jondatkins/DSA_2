def edit_distance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                vals = [matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]]
                min_val = min(vals)
                matrix[i][j] = min_val + 1
    return matrix[n - 1][m - 1]
