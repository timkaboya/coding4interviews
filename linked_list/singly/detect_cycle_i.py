'''
141. Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def detectCycle(head: Node) -> bool:
    '''time - O(n), space - O(n)'''

    curr = head
    _hash = set()

    while curr:
        if curr in _hash:
            return True

        _hash.add(curr)
        curr = curr.next

    return False


def detectCycle_v2(head: Node) -> bool:
    '''
    https://www.codesdope.com/blog/article/detect-a-loop-in-linked-list-using-floyds-cycle/
    Floyd's Cycle-Finding Algorithm
    time - O(n), space - O(1)
    '''

    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # move slow by one
        fast = fast.next.next  # move fast by two

        if slow == fast:
            return True

    return False
