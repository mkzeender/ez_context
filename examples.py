from random import random
from ez_context import context_mgr
from typing import assert_type


@context_mgr
def foo(bar: int = 10):
    print(f"entering {bar}")

    error = yield bar + 2

    print(f"exiting {bar}, {error=}")


with foo(10) as bar:
    assert_type(bar, int)
    assert bar == 12


@context_mgr
def random_value():
    rand_num = random()
    print(f"entering {rand_num}")

    error = yield rand_num

    print(f"exiting {rand_num}, {error=}")
    if isinstance(error, ValueError):
        return True  # suppress the error


# Parentheses are optional!
with random_value as r1:
    assert_type(r1, float)

    # reusable and reentrant
    with random_value:
        raise ValueError("CoolBeans")
