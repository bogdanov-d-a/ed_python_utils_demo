from edpu.calc_time_utils import *

print(hm_to_m(2, 15))
print(m_to_hm(135))
print(parse_time_point('02:15'))
print(parse_duration('2h 15m'))
print(time_point_string(135))
print(duration_string(135))
print(duration_string_with_negative(135))
print(duration_string_with_negative(135, True))
print(duration_string_with_negative(-135))
