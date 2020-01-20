if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    _t = arr[0]
    for i in range(len(arr)):
        if arr[i] != _t:
            print(arr[i])
            break
