import random

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse(root):
    if not root:
        return 0
    if root.left:
        if root.left.data > root.data:
            return 1
    if root.right:
        if root.right.data < root.data:
            return 1
    return traverse(root.left) + traverse(root.right)

def checkBST(root):
    if traverse(root) > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    l = [i for i in range(10)]
    rt = node(6)
    r = rt
    for i in range(10):
        if i < 10/2:
            r.left = node(i)
            r.right = None
        else:
            r.right = node(i)
            r.left = None
    if checkBST(rt):
        print('Yes')
    else:
        print('No')

    l = [i for i in range(10)]
    rt = node(6)
    r = rt
    for i in range(10):
        if i < 10/2:
            r.right = node(i)
            r.left = None
        else:
            r.left = node(i)
            r.right = None
    if checkBST(rt):
        print('Yes')
    else:
        print('No')
