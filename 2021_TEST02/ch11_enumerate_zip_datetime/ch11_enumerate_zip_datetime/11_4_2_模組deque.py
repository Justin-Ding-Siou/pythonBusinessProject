from collections import deque

nums = [i for i in range(1,6)]

# deque(iterable): 建立 deque 物件
dq = deque(nums)
print(dq)

# dq.rotate(n): deque 向右轉 n 個位置， 移除部分補到deque左邊
dq.rotate(1)
print(dq)

# dq.pop(): 移除 deque 物件最右邊元素
dq.pop()
print(dq)

# dq.popleft(): 移除 deque 物件最左邊元素
dq.popleft()
print(dq)

# dq.append(x): 在deque 物件右邊加入 x 元素
dq.append(8)
print(dq)

# dq.appendleft(x): 在 deque 物件左邊加入 x 元素
dq.appendleft(8)
print(dq)

print(dq.count(8))

# # dq.reverse(): 反轉 deque 物件
dq.reverse()
print(dq)