t = int(input())
while t > 0:
    n = int(input())
    a = input()
    stack = []
    for i in a:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    else:
        if stack:
            print("NO")
        else:
            print("YES")
    t -= 1
