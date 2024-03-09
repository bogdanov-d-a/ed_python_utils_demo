def main() -> None:
    from edpu import storage_finder

    print(storage_finder.get_drive_letters())
    print(storage_finder.find_all_storage())


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
