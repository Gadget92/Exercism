def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Variable not equals!')
    else:
        dist = 0
        zipped = zip(strand_a, strand_b)
        for a,b in list(zipped):
            if a != b:
                dist += 1
        return dist
