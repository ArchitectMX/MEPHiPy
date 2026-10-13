def balancedBrackets(s):
    stack = []
    d = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if d[stack[-1]] == i:
                stack.pop(-1)
            else:
                return False

    if len(stack) == 0:
        return True
    return False


print(balancedBrackets("([]){}"))
