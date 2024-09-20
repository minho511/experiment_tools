
# To minimize the number of characters in the markdown format table,
# remove spaces (' ') and eliminate redundant hyphens(-).

while True:
    s = ""
    while True:
        a = input()
        if a == "0":
            break
        for _ in range(100):
            a = a.replace('--', '-')

        s+=a.replace(" ", "") + '\n'
    print(s)

