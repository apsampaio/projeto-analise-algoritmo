def merge(A: list, aux: list, start: int, mid: int, end: int):
    for k in range(start, end + 1):
        aux[k] = A[k]

    i = start
    j = mid + 1

    for k in range(start, end + 1):
        if i > mid:
            A[k] = aux[j]
            j += 1
        elif j > end:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def mergesort(A, aux, start, end):
    if end <= start:
        return

    mid = (start + end) // 2
    mergesort(A, aux, start, mid)   # left
    mergesort(A, aux, mid + 1, end)  # end
    merge(A, aux, start, mid, end)


if __name__ == "__main__":
    ttl = int(input())
    tst = []

    for _ in range(ttl):
        t = input()
        tst.append(t)

    for t in tst:
        arr = t.split(" ")
        slots = int(arr[0])
        users = int(arr[1])

        grade = [float(x) for x in arr[2:]]
        mergesort(grade, [0] * len(grade), 0, len(grade) - 1)
        print(f"%.2f" % grade[-slots])
