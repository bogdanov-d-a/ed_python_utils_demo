def main() -> None:
    from edpu import input_password

    # salt generate: os.urandom(32)
    # password: test1234
    print(input_password.get_and_verify_password(
        b'l\xb3\x84R/\xd5\xb8\xe2\rM\xcf\xb5\xc5)\xdd\xb1Ox\xfa\xb4\xb3\xf4j\xf0\xaa\x10\xe2iG\xc4\x13\xd8',
        b'^\x99T\xf2TQ\xbc\xa85\x9fr\xb9\x96\x15\xdc\xe4\xbf>ZWN\x03\x8d\xef\x87G\xbf\xb9\xc0\xae\xaag'
    ))


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
