if __name__ == '__main__':
    n, m = input().split()
    l = input().split()
    a = set(input().split())
    b = set(input().split())


    print(sum((i in a) - (i in b) for i in l))
