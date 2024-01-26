def digital_root(n):
    if n > 9:
        n = sum([int(i) for i in str(n)])
        return digital_root(n)

    else:
        return n