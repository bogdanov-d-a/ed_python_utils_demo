def main() -> None:
    from edpu import calc_time_utils

    print(calc_time_utils.hm_to_m(2, 15))
    print(calc_time_utils.m_to_hm(135))
    print(calc_time_utils.parse_time_point('02:15'))
    print(calc_time_utils.parse_duration('2h 15m'))
    print(calc_time_utils.time_point_string(135))
    print(calc_time_utils.duration_string(135))
    print(calc_time_utils.duration_string_with_negative(135))
    print(calc_time_utils.duration_string_with_negative(135, True))
    print(calc_time_utils.duration_string_with_negative(-135))


if __name__ == '__main__':
    from edpu import pause_at_end
    pause_at_end.run(main, pause_at_end.DEFAULT_MESSAGE)
