from threading import RLock, Thread
from time import sleep
from ez_context import context_mgr

_next_num = 0
_num_lock = RLock()


@context_mgr
def unique_num():
    global _next_num
    with _num_lock:
        num = _next_num
        _next_num += 1

    print(f"entering with {num=}")

    yield num
    print(f"exiting with {num=}")


def main_thread():
    with unique_num:
        sleep(1)

    sleep(1)


def other_thread():
    sleep(0.5)
    with unique_num:
        sleep(1)


# should go in order of 0, 1, 0, 1.
Thread(target=other_thread, daemon=True).start()
main_thread()
