from typing import Any

class Stack:
    def __init__(self, stack_list: list):
        self.stack_list = stack_list

    def is_empty(self) -> bool:
        return not self.stack_list

    def push(self, new_element: Any):
        self.stack_list.append(new_element)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        last_element = self.stack_list.pop()
        return last_element

    def peek(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list[-1]

    def size(self) -> int:
        return len(self.stack_list)