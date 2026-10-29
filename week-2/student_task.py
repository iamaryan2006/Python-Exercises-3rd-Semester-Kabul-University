from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


int_stack = Stack[int]()
int_stack.push(10)
int_stack.push(20)
int_stack.push(30)

print(int_stack.peek())
print(int_stack.pop())
print(int_stack.size())
print(int_stack.is_empty())

str_stack = Stack[str]()
str_stack.push("Python")
str_stack.push("Java")
str_stack.push("C++")

print(str_stack.peek())
print(str_stack.pop())
print(str_stack.size())

empty_stack = Stack[int]()

try:
    empty_stack.pop()
except IndexError as e:
    print(e)
