class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
    
    def remove_elements(self, head, value):
        initial_node = ListNode(7)
        initial_node.next = head
        current_node = initial_node
        while current_node.next:
            if current_node.next.val == value:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return initial_node.next
