from collections import deque
import re


def encode(text):
    d = deque(list(text))
    first_symb = d.popleft()
    result = []

    current_symbol = f'{first_symb}'
    while d:
        symb = d.popleft()

        if current_symbol[-1] != symb:
            result.append((current_symbol[-1], len(current_symbol)))
            current_symbol = ''
            current_symbol += symb
        else:
            current_symbol += symb

        if not d:
            result.append((current_symbol[-1], len(current_symbol)))
            break

    return ''.join(f"{char}{count}" if count > 1 else char for char, count in result)



print(encode("аAACABCCS"))
