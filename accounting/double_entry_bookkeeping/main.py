from edpu.accounting.double_entry_bookkeeping import main
import edpu.pause_at_end


def run_operations(am):
    am.add_account('init_discrepancy')
    am.add_account('food_expense')
    am.add_account('debit_card')
    am.add_account('alice_debt')

    def init(target, amount):
        am.transfer('init_discrepancy', target, amount)

    init('debit_card', '10000')
    am.transfer('debit_card', 'food_expense', '600')
    am.transfer('debit_card', 'alice_debt', '2000')
    am.transfer('alice_debt', 'debit_card', '1000')


edpu.pause_at_end.run(lambda: main.run(run_operations))
