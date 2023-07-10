# Constant Time

$O(1)$

```py
def stupid_func()
    total = 1
    return total
```

# Linear Time

$O(n)$

```py
def sum(arr: list)
    total = 0
    for i in arr:
        total += i
    return total
```

# Logarithmic Time

$O(\log_2 n)$

```py
def bsearch(root, target):
    if not root:
        return False
    if target < root.val:
        return bsearch(root.left, target)
    elif target > root.val:
        return bsearch(root.right, target)
    else:
        return True
```
