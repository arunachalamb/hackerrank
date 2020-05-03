# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(l):
    while(l):
        print(l.val, end='->')
        l = l.next
    print('end')

def reverseKnodes(head: ListNode, k: int):
        _t = head
        _a = []
        while(_t):
            _a.append(_t.val)
            _t = _t.next
        _d = len(_a) // k
        _ra = []
        for i in range(_d):
            _tmp = _a[i*k:(i+1)*k]
            _tmp = _tmp[::-1]
            _ra += _tmp
        if len(_a) % k:
            _ra += _a[_d*k:]
        print(_ra)
        _h = ListNode()
        _head = _h
        for e in _ra[:-1]:
            _h.val = e
            _h.next = ListNode()
            _h = _h.next
        _h.val = _ra[-1]
        _h.next = None
        return _head

"""
if __name__ == '__main__':
    l = [1, 2, 3, 4]
    k = 2
    _head = ListNode()
    _h = _head
    for e in l[:-1]:
        _h.val = e
        _h.next = ListNode()
        _h = _h.next
    _h.val = l[-1]
    _h.next = None
    print_list(_head)
    _r = reverseKnodes(_head, k)
    print_list(_r)
"""
