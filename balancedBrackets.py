def balancedBrackets(string):
    stack = []
    posibilities = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in posibilities:
            top = stack.pop() if stack else "#"
            if posibilities[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
