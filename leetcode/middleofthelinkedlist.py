class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer solution would be something like fast.next.next and slow.next and return slow?
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
