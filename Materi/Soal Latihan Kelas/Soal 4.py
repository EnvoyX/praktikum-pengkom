a = int(input("Nilai A: "))
b = int(input("Nilai B: "))
c = int(input("Nilai C: "))


if a > b > c:
    print(f"{a},{b},{c}")
elif a > c > b:
    print(f"{a},{b},{c}")
elif b > a > c:
    print(f"{b},{a},{c}")
elif b > c > a:
    print(f"{b},{a},{c}")
elif c > b > a:
    print(f"{c},{b},{a}")
else:
    print(f"{c},{a},{b}")