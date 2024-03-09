if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(lambda: print('lambda run'), wait_on_success='success')
