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


def decode(text):
    """
    Decodes the text using run-length encoding
    """
    pattern = r"[A-Za-z]\d*"
    matches = re.findall(pattern, text)
    result = []

    for i in matches:
        result.append(i[0] * int(i[1:] if i[1:] else 1))

    return ''.join(result)


print(decode("A2BC3XCCDE4"))
