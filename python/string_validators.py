import re

if __name__ == '__main__':
    s = input()
    print(re.search(r'[a-zA-Z0-9]', s) != None)
    print(re.search(r'[a-zA-Z]', s) != None)
    print(re.search(r'[0-9]', s) != None)
    print(re.search(r'[a-z]', s) != None)
    print(re.search(r'[A-Z]', s) != None)
