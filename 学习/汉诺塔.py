steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps += 1
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
    else:
        hanoi(src, mid, des, n-1)
        steps += 1
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
        hanoi(mid, des, src, n-1)
N = eval(input())
hanoi("A", "C", "B", N)