def is_power_of_3(n):
    max_int = 2**32-1
    power = {}
    power[0] = 1
    power[1] = 3
    i = 2
    while power[i-1]*3 < max_int:
        power[i] = power[i-1]*3
        i += 1
    print power[20]
    for c in power.values():
        if c == n:
            return 1
    return 0

print is_power_of_3(27)
print is_power_of_3(3**9)
print is_power_of_3(1231234)
