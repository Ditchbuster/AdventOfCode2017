def day15():
    a     = 634
    b     = 301
    count = 0

    for i in range(0, 40000000):
      a = (a * 16807) % 2147483647
      b = (b * 48271) % 2147483647

      if ((a & 0xffff) == (b & 0xffff)):
        count += 1

    print ('%d' % (count))


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("day15()", setup="from __main__ import day15",number=1))