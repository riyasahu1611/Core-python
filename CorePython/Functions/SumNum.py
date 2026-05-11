def sumnum(a, *varg):
    t = a
    for n in varg:
        t += n
        return t

    total = sumnum(1, 2, 3, 4, 5)
    print('Total', total)
