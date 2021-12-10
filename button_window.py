from edpu import button_window

button_window.run([
    ('Button 1', lambda: print('Command 1')),
    ('Button 2', lambda: print('Command 2')),
    ('Button 3', lambda: print('Command 3')),
    ('Button 4', lambda: print('Command 4')),
])
