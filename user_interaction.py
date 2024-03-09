def main() -> None:
    from edpu import user_interaction

    print(user_interaction.yes_no_prompt('Yes or No Msg'))

    print(user_interaction.pick_option('Pick option', [
        'Option 1',
        'Option 2',
        'Option 3',
        'Option 4',
    ]))

    print(user_interaction.pick_option_multi('Pick options', [
        'Option 1',
        'Option 2',
        'Option 3',
        'Option 4',
    ]))


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
