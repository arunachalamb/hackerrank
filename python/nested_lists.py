if __name__ == '__main__':
    _l = 100
    _sl = 100
    stds = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stds.append([name, score])
    stds.sort(key=lambda x: x[1])
    _v = 0
    for e in stds:
        if e[1] != stds[0][1]:
            _v = e[1]
            break
    _f = list(filter(lambda x : x[1] == _v, stds))
    _f.sort(key=lambda x : x[0])
    for e in _f:
        print(e[0])
