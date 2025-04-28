from Stack import Stack


def checking(elems: str) -> str:
    stack = Stack([])
    dictionary_of_elements = {')': '(', ']': '[', '}': '{'}
    for elem in elems:
        if elem in dictionary_of_elements:
            top_element = stack.pop()
            if top_element is None or dictionary_of_elements[elem] != top_element:
                return "Не сбалансировано"
        else:
            stack.push(elem)
    return 'Сбалансировано'

