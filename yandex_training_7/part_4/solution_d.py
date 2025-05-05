from typing import Any, Self


class Deque:

    class Node:
        def __init__(
                self, val: Any = None,
                prev: Self | None = None,
                next: Self | None = None
        ):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = Deque.Node()
        self.tail = Deque.Node()
        self.clear()

    def push_front(self, val: Any):
        node = Deque.Node(val=val, prev=self.head, next=self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def push_back(self, val: Any):
        node = Deque.Node(val=val, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1

    def front(self):
        if not self._size:
            raise IndexError()
        return self.head.next.val

    def pop_front(self):
        val = self.front()
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self._size -= 1
        return val

    def back(self):
        if not self._size:
            raise IndexError()
        return self.tail.prev.val

    def pop_back(self):
        val = self.back()
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self._size -= 1
        return val

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def size(self):
        return self._size

    def __bool__(self):
        return bool(self._size)

    def __len__(self):
        return self._size

    def _detach(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        self._size -= 1
        return node

    def _attach_after(self, node, after):
        node.next = after.next
        node.prev = after
        after.next.prev = node
        after.next = node
        self._size += 1
        return node

    def _attach_before(self, node, before):
        node.next = before
        node.prev = before.prev
        before.prev.next = node
        before.prev = node
        self._size += 1
        return node


class Windows(Deque):
    def __init__(self):
        super().__init__()
        self.current = self.tail

    def push(self, name: str):
        self.current = self._attach_before(Deque.Node(name), self.current)
        return self.current.val

    def tab(self, count):
        count %= self._size
        while count:
            self.current = self.current.next
            if self.current is self.tail:
                self.current = self.head.next
            count -= 1
        self.current = self._attach_after(
            self._detach(self.current),
            self.head
        )
        return self.current.val


if __name__ == "__main__":
    programs = Windows()
    n = int(input())
    for _ in range(n):
        request = input()
        command = request[:3]
        if command == "Run":
            name = request[4:]
            print(programs.push(name))
        elif command == "Alt":
            count = request.count("+")
            print(programs.tab(count))
