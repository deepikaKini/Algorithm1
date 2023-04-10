def what_do_i_do(left, right):
    if left == right:
        return A[left] % 2, A[left] % 2, A[left] % 2
    else:
        m = (left + right) // 2
        llstreak, lrstreak, lmstreak = what_do_i_do(left, m)
        rlstreak, rrstreak, rmstreak = what_do_i_do(m + 1, right)

        maxstreak = max(lmstreak, rmstreak, lrstreak + rlstreak)

        if lmstreak == m - left + 1:
            lstreak = lmstreak + rlstreak
        else:
            lstreak = llstreak

        if rmstreak == right - m:
            rstreak = rmstreak + lrstreak
        else:
            rstreak = rrstreak

        return lstreak, rstreak, maxstreak


A = list(map(int, input().split(' ')))

print(what_do_i_do(0, len(A) - 1))
