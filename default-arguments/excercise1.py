import time


def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")


count(10)
