# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        hashTable = {}

        while curr:
            if curr in hashTable:
                return True
            else:
                hashTable[curr] = 1
                curr = curr.next
        return False
        
        