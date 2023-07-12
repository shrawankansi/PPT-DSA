def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for s_char, t_char in zip(s, t):
        if s_char not in s_to_t and t_char not in t_to_s:
            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char
        elif s_char in s_to_t and t_char in t_to_s:
            if s_to_t[s_char] != t_char or t_to_s[t_char] != s_char:
                return False
        else:
            return False

    return True
s = "egg"
t = "add"
result = isomorphic_strings(s, t)
print(result)