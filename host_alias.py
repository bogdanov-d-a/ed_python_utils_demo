def main() -> None:
    from edpu import host_alias
    print(host_alias.get())


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
