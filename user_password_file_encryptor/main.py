def main() -> None:
    from edpu import user_password_file_encryptor
    user_password_file_encryptor.encrypt('test.txt')


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
