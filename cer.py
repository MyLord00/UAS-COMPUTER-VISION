def calculate_cer(ground_truth, prediction):
    """
    Menghitung Character Error Rate (CER)
    beserta jumlah Substitution (S),
    Deletion (D), Insertion (I), dan
    jumlah karakter Ground Truth (N).
    """

    gt = ground_truth.upper().strip()
    pred = prediction.upper().strip()

    m = len(gt)
    n = len(pred)

    # Matriks Levenshtein
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Inisialisasi
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Isi matriks
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if gt[i - 1] == pred[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,          # Deletion
                dp[i][j - 1] + 1,          # Insertion
                dp[i - 1][j - 1] + cost    # Substitution
            )

    # ==========================
    # Backtracking
    # ==========================

    S = 0
    D = 0
    I = 0

    i = m
    j = n

    while i > 0 or j > 0:

        if i > 0 and j > 0 and gt[i - 1] == pred[j - 1]:
            i -= 1
            j -= 1

        elif (
            i > 0 and j > 0 and
            dp[i][j] == dp[i - 1][j - 1] + 1
        ):
            S += 1
            i -= 1
            j -= 1

        elif (
            i > 0 and
            dp[i][j] == dp[i - 1][j] + 1
        ):
            D += 1
            i -= 1

        else:
            I += 1
            j -= 1

    N = len(gt)

    CER = (S + D + I) / N if N > 0 else 0

    return CER, S, D, I, N