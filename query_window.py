from edpu import query_window

counter = 0

def data_provider():
    global counter
    counter += 1
    return 'data_provider: ' + str(counter)

query_window.run_with_exception_wrapper(data_provider)
