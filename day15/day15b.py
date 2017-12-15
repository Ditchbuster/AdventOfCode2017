def day15b():
    gena = 873
    genb = 583

    #gena = 65
    #genb = 8921

    ad = 16807
    bd = 48271
    d = 2147483647
    count = 0
    bl = []
    al = []
    while min(len(bl),len(al))<5000000:
        gena = int((gena * ad) % d)
        genb = int((genb * bd) % d)
        if gena % 4 == 0:
            al.append(gena)
        if genb % 8 == 0:
            bl.append(genb)

    for i in range(min(len(al),len(bl))):
        if bin(al[i])[-16:] == bin(bl[i])[-16:]:
            count += 1

    print(count)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("day15b()", setup="from __main__ import day15b", number=1))