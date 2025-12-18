#1
with open("users.txt", "r") as file:
    for line in file:
        print(line.strip())
#2
with open("passwords.txt", "r") as inp, open("weak.txt", "w") as out:
    for password in inp:
        if len(password.strip()) < 8:
            out.write(password)
#3
with open("ips.txt", "r") as inp:
    unique_ips = set(inp)

with open("unique_ips.txt", "w") as out:
    for ip in unique_ips:
        out.write(ip)
#4
with open("log.txt", "r") as file:
    count = sum(1 for _ in file)

print(count)
#5
with open("ports.txt", "r") as inp, open("blocked_ports.txt", "w") as out:
    for port in inp:
        if int(port.strip()) < 1024:
            out.write(port)
#6
with open("auth.log", "r") as inp, open("failed.txt", "w") as out:
    for line in inp:
        if "fail" in line.lower():
            out.write(line)
#7
with open("traffic.txt", "r") as inp, open("alert.txt", "w") as out:
    for value in inp:
        if int(value.strip()) > 1000:
            out.write(value)
#8
with open("commands.txt", "r") as inp, open("safe.txt", "w") as out:
    for cmd in inp:
        if "rm" not in cmd:
            out.write(cmd)
#9
with open("users.txt", "r") as file:
    count = sum(1 for _ in file)

with open("report.txt", "w") as report:
    report.write(f"Всего пользователей: {count}")
#10
with open("full_log.txt", "w") as out:
    for name in ["log1.txt", "log2.txt"]:
        with open(name, "r") as file:
            out.write(file.read())