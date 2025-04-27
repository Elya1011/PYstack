from Stack import Stack


def checking(elems: str) -> str:
    stack = Stack([])
    dictionary_of_elements = {')': '(', ']': '[', '}': '{'}
    for elem in elems:
        if elem in dictionary_of_elements:
            top_element = stack.pop() if not stack.is_empty() else '#'
            if dictionary_of_elements[elem] != top_element:
                return "Не сбалансировано"
        else:
            stack.push(elem)
    return 'Сбалансировано'

