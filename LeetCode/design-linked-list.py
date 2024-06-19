class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.node = None
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.node
        for _ in range(index):
            current = current.next
        return current.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.node
        self.node = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.node:
            self.node = new_node
        else:
            current = self.node
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            prev = self.node
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.node = self.node.next
        else:
            prev = self.node
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
        self.length -= 1


class Node:
    def __init__(self, data=None):
        self.value = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, object):
        self._next = object

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
