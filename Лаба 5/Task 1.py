f = open("input.txt", "r")
g = open("output.txt", "w")

for n in f:
    l = n.find("{")
    r = n.find("}")
    if l == -1 or r == -1:
        g.write(n)
        continue
    n_new = n[:l] + n[r + 1:]

    while n_new.count("{") > 0:
        l = n_new.find("{")
        r = n_new.find("}")
        n_new = n_new[:l] + n_new[r + 1:]
    g.write(n_new)
