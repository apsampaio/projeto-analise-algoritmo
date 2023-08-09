# Andre Sampaio
# Thayná Andressa

def selection(arr: list, x: float):
    for i in range(len(arr)):
        if x > arr[i]:
            arr.insert(i, x)
            arr.pop()
            break


if __name__ == "__main__":
    ttl = int(input())
    tst = []

    for _ in range(ttl):
        t = input()
        tst.append(t)

    for t in tst:
        arr = t.split(" ")
        slots = int(arr[0])
        filler = [1] * slots
        for i in arr[2:]:
            selection(filler, float(i))
        print(f"%.2f" % filler[-1])
