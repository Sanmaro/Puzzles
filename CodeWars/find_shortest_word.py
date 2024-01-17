def find_short(s):
    s_list = s.split()
    return len(min(s_list, key=len))

print(find_short("bitcoin take over the world maybe who knows perhaps"))