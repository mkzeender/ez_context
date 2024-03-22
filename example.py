from ez_context import context_mgr


@context_mgr
def suppress_and_print():
    print("entering")
    error = yield
    print(error)
    return True  # suppress error


with suppress_and_print:
    raise Exception("Hello")
