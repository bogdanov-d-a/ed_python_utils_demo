def main() -> None:
    from edpu import report_maker

    def report_processor(path):
        return 'report_processor: ' + path

    report_maker.make_reports(
        ['data1', 'data2'],
        report_processor
    )


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
