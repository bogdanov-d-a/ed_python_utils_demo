def main() -> None:
    import edpu.datetime_utils
    print(edpu.datetime_utils.get_now_datetime_str())


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
