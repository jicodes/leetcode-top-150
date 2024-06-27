class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        self.head = ListNode()  # dummy head
        self.tail = ListNode()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self._remove(node)
            self._insert(node)
        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._insert(new_node)

            if len(self.cache) > self.capacity:
                tail = self.tail.prev
                self._remove(tail)
                del self.cache[tail.key]
