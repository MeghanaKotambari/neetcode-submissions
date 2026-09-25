class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Create copy nodes and insert them after original nodes
        curr = head

        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2. Set random pointers of copied nodes
        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Separate original and copied lists
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head