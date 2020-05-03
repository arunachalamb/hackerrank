# merge 2 sorted arrays

def merge_sorted(a, b):
    _ia = 0
    _ib = 0
    _r = []
    for i in range(len(a) + len(b)):
        if a[_ia] < b[_ib]:
            _r.append(a[_ia])
            _ia += 1
        else:
            _r.append(b[_ib])
            _ib += 1
        if _ia == len(a):
            for j in range(_ib, len(b)):
                _r.append(b[j])
            break
        if _ib == len(b):
            for j in range(_ia, len(a)):
                _r.append(a[j])
            break
    return _r
