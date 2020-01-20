from collections import OrderedDict

def merge_the_tools(string, k):
    string = [string[i:i+k] for i in range(0, len(string), k)]
    string = list(map(lambda x : ''.join(OrderedDict.fromkeys(x)), string))
    for s in string:
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
