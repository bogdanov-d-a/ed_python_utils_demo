def main() -> None:
    from edpu import explorer_launcher
    explorer_launcher.open_dir_in_explorer(r'C:\Program Files')


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
