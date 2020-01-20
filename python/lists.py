if __name__ == '__main__':
    N = int(input())
    _l = []
    _o = []
    for i in range(N):
        _l.append(input().split())

    for c in _l:
        if c[0] == 'print':
            print(_o)
        else:
            eval("_o.{0}(".format(c[0]) + ",".join([i for i in c[1:]]) + ")")
