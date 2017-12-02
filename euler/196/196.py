
a, b = input().strip().split(' ')
a, b = int(a), int(b)

out = 0
for c in (a, b):
    #print(c)
    ol = []
    if c == 1:
        continue
    elif c == 2:
        out += 5
        continue
    def start_num(seq):
        start = 1
        for i in range(1, seq+1):
            start += i - 1
        return start

    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    cs = start_num(c)
    ce = cs + c - 1
    cps = [i for i in range(cs, ce+1) if is_prime(i)]
    #print(cps)
    ps = start_num(c-1)
    pe = ps + c - 2
    pps = [i for i in range(ps, pe+1) if is_prime(i)]
    #print(pps)
    ns = start_num(c+1)
    ne = ns + c
    nps = [i for i in range(ns, ne+1) if is_prime(i)]
    #print(nps)
    p2s = start_num(c-2)
    p2e = p2s + c - 3
    p2ps = [i for i in range(p2s, p2e+1) if is_prime(i)]
    #print(p2ps)
    n2s = start_num(c+2)
    n2e = n2s + c + 1
    n2ps = [i for i in range(n2s, n2e+1) if is_prime(i)]
    #print(n2ps)

    def gen_match_set(n, r, s, e): # number, sequence, seq start, seq end
        if r%2:
            l = [n-r+1,  n+r+1, n+r-1]
            if n-r+1 >= s:
                l.remove(n-r+1)
            if n+r-1 <= e:
                l.remove(n+r-1)
        else:
            l = [n-r, n-r+2, n+r]
            if n-r < s-r+1:
                l.remove(n-r)
            if n-r+2 >= s:
                l.remove(n-r+2)
        return l

    for i in range(cs, cs + c):
        n = 0
        if i not in cps:
            continue
        for j in gen_match_set(i, c, cs, ce):
            if j in cps:
                n += 1
            elif j in pps:
                n += 1
                if c%2:
                    if (j-c+1) in p2ps or (j-c+3) in p2ps:
                        n = 2
                        break
                else:
                    if (j-c+2) in p2ps:
                        n = 2
                        break
            elif j in nps:
                n += 1
                if c%2:
                    if (j+c+1) in p2ps or (j+c+2) in p2ps:
                        n = 2
                        break
                else:
                    if (j+c) in p2ps:
                        n = 2
                        break
            #print(j, n)
        if n >= 2:
            ol.append(i)
    #print('out list')
    #print(ol)
    out += sum(ol)
print(out)
