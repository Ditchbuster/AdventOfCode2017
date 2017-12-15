def day15():
    gena = 873
    genb = 583

    ad = 16807
    bd = 48271
    d = 2147483647
    count = 0
    for i in range(40000000):
        gena = int((gena * ad) % d)
        genb = int((genb * bd) % d)
        if bin(gena)[-16:] == bin(genb)[-16:]:
            count += 1

    print(count)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("day15()", setup="from __main__ import day15",number=1))