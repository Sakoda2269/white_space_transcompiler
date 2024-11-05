t = "\t"
n = "\n"
s = " "

def num_to_white(numstr: str):
    num = int(numstr)
    res = []
    if num < 0:
        res.append(t)
        num = -num
    else:
        res.append(s)
    bit = bin(num)[2:]
    for c in bit:
        if c == "1":
            res.append(t)
        else:
            res.append(s)
    res.append(n)
    return "".join(res)