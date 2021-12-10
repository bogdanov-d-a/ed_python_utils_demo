from edpu import checklist_tool

data = [
    ('Checklist A', [
        'Item A1',
        'Item A2',
        'Item A3',
        'Item A4',
    ]),
    ('Checklist B', [
        'Item B1',
        'Item B2',
    ]),
]

checklist_tool.show_picker(data)
