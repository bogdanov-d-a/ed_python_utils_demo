from edpu.accounting import single_entry_bookkeeping
from edpu.accounting.data.decimal import DecimalData

print(single_entry_bookkeeping.get_info(
    [
        ('give', '4242', 'note 1'),
        ('give', '228', 'note 2'),
        ('take', '1337', 'note 3'),
    ],
    DecimalData,
    single_entry_bookkeeping.get_debt_subject_area()
))
