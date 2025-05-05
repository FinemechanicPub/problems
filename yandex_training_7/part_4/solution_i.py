import sys


if __name__ == "__main__":
    reader = sys.stdin.readline
    stack, top = [0], [0]
    n = int(reader())
    for _ in range(n):
        t, m = map(int, reader().split())
        if m == 0:
            while t and stack[t] == stack[top[t]]:
                t = top[t]
            t = top[t]
        stack.append(stack[t] + m)
        top.append(t)
    print(sum(stack))
