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

def mergeKLists(lists): #List[ListNode]) -> ListNode:
        if not len(lists):
            return None
        for ix, e in enumerate(lists):
            if e:
                _r = e
                break
        else:
            return None
        for i in range(ix+1, len(lists)):
            print('New List')
            _t = lists[i]
            _l = _r
            print_list(_l)
            print_list(_t)
            if not _t:
                continue
            while(_t):
                _tmp = _l
                while(_l.val <= _t.val):
                     print(_l.val, _t.val)
                     _tmp = _l
                     _l = _l.next
                     if not _l:
                         break
                if _tmp.val <= _t.val:
                    print('tmp < _t', _tmp.val, _t.val)
                    _n = _tmp.next
                    _tmp.next = ListNode(_t.val)
                    _tmp.next.next = _n
                    _l = _tmp.next
                else:
                    print('tmp > _t', _tmp.val, _t.val)
                    _h = ListNode(_t.val)
                    _r = _h
                    _h.next = _tmp
                    _l = _r
                _t = _t.next
            print_list(_t)
            print_list(_l)
        return _r

"""
if __name__ == '__main__':
    l = [[-1, -1, -1], [-2, -2, -1]]
    ll = []
    for i in l:
        _h = ListNode()
        ll.append(_h)
        _n = _h
        for j in i:
            _n.val = j
            _n.next = ListNode()
            _p = _n
            _n = _n.next
        del _n
        _p.next = None
    for i in ll:
        print_list(i)
    print('Merge')
    _r = mergeKLists(ll)
    print_list(_r)
"""
