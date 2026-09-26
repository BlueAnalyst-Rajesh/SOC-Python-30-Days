with open("security.log", "r") as file:
    for line in file:
        if "AUTH_FAIL" in line:
            parts = line.split()
            ip_part = parts[4]
            ip = ip_part.split("=")
            print(ip[1])
