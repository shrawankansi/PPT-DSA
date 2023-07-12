def can_shift(s, goal):
    if len(s) != len(goal):
        return False

    s2 = s + s
    if goal in s2:
        return True
    else:
        return False
s = "abcde"
goal = "cdeab"
print(can_shift(s, goal))
