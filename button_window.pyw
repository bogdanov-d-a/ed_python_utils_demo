def main() -> None:
    from edpu import button_window

    def handler(str_: str) -> None:
        from edpu.tkinter_utils import showinfo
        showinfo(str_)

    button_window.run([
        ('Button 1', lambda: handler('Command 1')),
        ('Button 2', lambda: handler('Command 2')),
        ('Button 3', lambda: handler('Command 3')),
        ('Button 4', lambda: handler('Command 4')),
    ])


if __name__ == '__main__':
    from edpu.tkinter_utils import handle_errors
    handle_errors(main)
