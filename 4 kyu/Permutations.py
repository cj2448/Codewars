def permutations(string):
    if (len(string) == 1):
        return [string]

    perm_set = set()
    for char in string:
        [perm_set.add(char + a) for a in permutations(string.replace(char, "", 1))]
    return list(perm_set)