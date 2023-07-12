def reconstruct_permutation(s):
    n = len(s)
    current = 0
    perm = []

    for ch in s:
        if ch == 'I':
            perm.append(current)
            current += 1
        else:  # ch == 'D'
            perm.insert(current, n)
            n -= 1
            current += 1

    perm.append(current)

    return perm
s = "IDID"
result = reconstruct_permutation(s)
print(result)