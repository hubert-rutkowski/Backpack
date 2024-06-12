def dynamic_programming(C, items):
    n = len(items)
    dp = [[0] * (C + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, volume = items[i - 1][0], items[i - 1][1]
        for j in range(1, C + 1):
            if volume <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - volume] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, C
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    return dp[n][C], selected_items[::-1]