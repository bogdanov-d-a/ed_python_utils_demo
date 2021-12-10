from edpu import report_maker

def report_processor(path):
    return 'report_processor: ' + path

report_maker.make_reports(
    ['data1', 'data2'],
    report_processor
)
