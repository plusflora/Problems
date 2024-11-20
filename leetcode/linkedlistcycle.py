# this looks like we're trying to figure out if the position is possible in the list
# okay - the question itself was worded in a shitty way. it appears to give the position as an input in the examples despite the description of the problem saying it's not passed as an argument.
# first thought is to step through the list and if we se the

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we need a way to check if we've already visited this node.
        seen = set()
        # we need a starting point - the head of the list
        current = head
        # we want to iterate through the list -
        while current:
            # if we run into the node - we return True
            if current in seen:
                return True
            # if we don't see the "current" node in "seen" - we add the "current" node to "seen" - then proceed down the list.
            seen.add(current)
            current = current.next
        # if we don't see it when current becomes none - return False
        return False
