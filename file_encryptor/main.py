def main() -> None:
    from edpu import file_encryptor
    file_encryptor.encrypt('data.txt', 'password', 'data.7z')


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
