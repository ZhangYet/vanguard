class ListedNode:

    def __init__(self, val: int):
        self.val = val
        self.next = self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dump_head = ListedNode(-1)
        self.dump_tail = ListedNode(-1)
        self.dump_head.next = self.dump_tail
        self.dump_tail.prev = self.dump_head
        self.length = 0

    # def debug(self):
    #     res = []
    #     if not self.length:
    #         print(res)
    #         return
    #
    #     for i in range(self.length):
    #         node = self._get(i)
    #         res.append(node.val)
    #
    #     print(res.reverse())

    def get(self, index: int) -> int:
        return self._get(index).val

    def _get(self, index: int) -> ListedNode:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == -1:
            return self.dump_head
        curr: ListedNode = self.dump_head
        for _ in range(index+1):
            if not curr.next:
                return curr
            curr: ListedNode = curr.next

        return curr

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node: ListedNode = ListedNode(val)
        new_node.prev = self.dump_head
        new_node.next = self.dump_head.next
        self.dump_head.next.prev = new_node
        self.dump_head.next = new_node
        self.length += 1
        # self.debug()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node: ListedNode = ListedNode(val)
        new_node.next = self.dump_tail
        new_node.prev = self.dump_tail.prev
        self.dump_tail.prev.next = new_node
        self.dump_tail.prev = new_node
        self.length += 1
        # self.debug()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return None

        if index == self.length:
            return self.addAtTail(val)

        new_node = ListedNode(val)
        prev_node = self._get(index-1)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1
        # self.debug()

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr_node = self._get(index)
        if curr_node.val == -1:
            return

        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        self.length -= 1
        # self.debug()
        return
