def main() -> None:
    from edpu import query_window

    counter = 0

    def data_provider():
        nonlocal counter
        counter += 1
        return 'data_provider: ' + str(counter)

    query_window.run_with_exception_wrapper(data_provider)


if __name__ == '__main__':
    from edpu.tkinter_utils import handle_errors
    handle_errors(main)
