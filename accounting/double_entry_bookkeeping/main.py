def main() -> None:
    from decimal import Decimal
    from edpu.accounting.data.decimal import DecimalData
    from edpu.accounting.double_entry_bookkeeping.main import run
    from edpu.accounting.double_entry_bookkeeping.account_manager import AccountManager

    def run_operations(am: AccountManager[Decimal]) -> None:
        am.add_account('init_discrepancy')
        am.add_account('food_expense')
        am.add_account('debit_card')
        am.add_account('alice_debt')

        def init(target: str, amount: str) -> None:
            am.transfer('init_discrepancy', target, amount)

        init('debit_card', '10000')
        am.transfer('debit_card', 'food_expense', '600')
        am.transfer('debit_card', 'alice_debt', '2000')
        am.transfer('alice_debt', 'debit_card', '1000')

    run(DecimalData(), run_operations)


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
