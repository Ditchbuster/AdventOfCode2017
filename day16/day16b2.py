
def day16():
    r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    x = [7,12,4,5,0,9,13,6,15,11,10,8,3,14,2,1]
    for i in range(10):
        r = [r[7],r[12],r[4],r[5],r[0],r[9],r[13],r[6],r[15],r[11],r[10],r[8],r[3],r[14],r[2],r[1]]
    print(''.join(r))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("day16()", setup="from __main__ import day16",number=1))

    import itertools

    r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    print(len(list(itertools.permutations(r))))
