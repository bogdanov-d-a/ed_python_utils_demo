from edpu import user_interaction

print(user_interaction.yes_no_prompt('Yes or No Msg'))

print(user_interaction.pick_option('Pick option', [
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4',
]))
