from collections import OrderedDict

if __name__ == '__main__':
    _d = OrderedDict()
    n = int(input())
    for i in range(n):
        k = input()
        if k in _d:
            _d[k] += 1
        else:
            _d[k] = 1
    v = ' '.join(str(_d[k]) for k in _d)
    print(len(_d))
    print(v)
