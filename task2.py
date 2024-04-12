from collections import deque

source = input()
length = len(source)
out = [" "]*length
queue = deque()

for i in range(length):
    if source[i] == ('('):
        queue.append(i)
    elif source[i] == ')':
        if len(queue) > 0:
            queue.popleft()
        else: out[i]="?"

while len(queue) > 0:
    out[queue.popleft()] = "x"
print(source)
print("".join(out))

