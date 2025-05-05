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


class Stack(Deque):
    def __init__(self):
        super().__init__()

    def push(self, val: Any):
        return self.push_back(val)

    def pop(self):
        return self.pop_back()


if __name__ == "__main__":
    stack = Stack()
    while True:
        command, *args = input().split()
        if command == "exit":
            break
        try:
            result = getattr(stack, command)(*args)
            print(result if result is not None else "ok")
        except IndexError:
            print("error")
    print("bye")
