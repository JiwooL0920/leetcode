# ou are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Time: O(N)
# Mem: O(1)

# two pointers, one in beginning one at end 
# take first half and second half of list and alternate 
# for entire second half, reverse the link and then perform operations 
# finding half point -> slow and fast pointer. shift slow pointer by one, fast pointer by two. even list -> slow.next = beginning of second list; odd list -> slow.next = second half first element, fast at tail.next=null 

class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next # second half 
        prev = slow.next = None # split link between first half and second half 
        # now reverse second list 
        while second:
            tmp = second.next
            second.next = prev 
            prev = second
            second = tmp 
        # merge two halfs 
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1 #inserting second between first and first.next
            first, second = tmp1, tmp2 
        
        