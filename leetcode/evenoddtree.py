# so level 0 is odd - level 1 (and all odd levels from here on out) contains [odd] numbers and it has to decrease ie [10, 4] - level 2 (and all even levels from here on out) contains [even] numbers
# level 0         1
#                / \
# level 1      10   4
#             / \  / \
# level 2   3   5|7   9
#
# So we want to go something like -
# I want a way to figure out if the level is even or odd - boolean?
even = True

q = deque([root])

while q:
    prev = float("inf")
    for x in range(len(q)):
        node = q.popleft()

        if even and (node.val % 2 == 0 or node.val <= prev):
            return False

        elif not even and (node.val % 2 == 1 or node.val >= prev):
            return False
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        prev = node.val
    even = not even
return True
