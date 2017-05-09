# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = node = ListNode(0)
        i = 0
        while l1 or l2 or i:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            temp = val1 + val2 + i
            i = temp / 10
            node.next = ListNode(temp % 10)
            node = node.next
        
        return root.next
                
            
