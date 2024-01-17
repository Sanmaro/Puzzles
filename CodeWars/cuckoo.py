def cuckoo_clock(initial_time, n):
    hours = int(initial_time.split(":")[0]) 
    minutes = int(initial_time.split(":")[1]) 
    chimes = 0
    while chimes < n:
        if minutes == 0:
            chimes += hours
        elif minutes == 15 or minutes == 30 or minutes == 45:
            chimes += 1

        minutes += 1 
        if minutes > 59:
             hours += 1
             minutes -= 60
        if hours > 12:
            hours -= 12
    return f"{hours:02d}:{(minutes - 1):02d}"

print(cuckoo_clock("04:01", 10))
