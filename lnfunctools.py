import time
from functools import cache


@cache
def ex_func(num):
    st = time.perf_counter()
    time.sleep(1)
    tl = time.perf_counter() - st
    return round(tl)


if __name__ == "__main__":
    st = time.perf_counter()
    call_3 = ex_func(3)
    ed = time.perf_counter()
    print(call_3, round(ed - st))

    st = time.perf_counter()
    call_3 = ex_func(3)
    ed = time.perf_counter()
    print(call_3, round(ed - st))

    st = time.perf_counter()
    call_3 = ex_func(3)
    ed = time.perf_counter()
    print(call_3, round(ed - st))
