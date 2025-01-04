def isValid(s: str) -> bool:
    parentheses = {")": "(", "}": "{", "]": "["}
    stack = []
    for p in s:
        if p in parentheses:
            if parentheses[p] != stack.pop():
                return False
        else:
            stack.append(p)
    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    assert isValid("()") == True, f"Expected True, got {isValid('()')}"
    assert isValid("()[]{}") == True, f"Expected True, got {isValid('()[]{}')}"
    assert isValid("(]") == False, f"Expected False, got {isValid('(]')}"
    assert isValid("([)]") == False, f"Expected False, got {isValid('([)]')}"
    assert isValid("{[]}") == True, f"Expected True, got {isValid('{[]}')}"
    assert isValid("") == True, f"Expected True, got {isValid('')}"
    assert isValid("(((((") == False, f"Expected False, got {isValid('(((((')}"
