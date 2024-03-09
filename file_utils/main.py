def main() -> None:
    from edpu import file_utils

    file_utils.create_and_open_dir_with_datetime('.')
    print(file_utils.eval_file('eval.txt'))


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
