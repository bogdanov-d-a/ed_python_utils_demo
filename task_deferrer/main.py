def main() -> None:
    from edpu import task_deferrer

    task_deferrer.info_viewer('data.py')
    task_deferrer.info_2d_viewer('data_2d.py')


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
