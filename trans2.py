from collections import deque

class ReadError(Exception): ...
    
t = "\t"
n = "\n"
s = " "

def read_program(lines_in: str, ans: list):
    lines = deque(map(lambda x: x + "\n", lines_in.split("\n")))
    for l in lines:
        o, a, s = read_line(l)
        if s == 0:
            parser(o, a, ans)
        

reserved = {"for", "while", "if", "ok", "ng"}

def read_line(line_in: str):
    if not line_in:
        return "", [], -1
    if len(line_in) == 0:
        return "", [], -1
    line = deque(line_in)
    if line[0] == " ":
        line.popleft()
    ope_list = []
    while True:
        if not line:
            raise ReadError("\"(\" was not found")
        c = line.popleft()
        if c == "(":
            break
        ope_list.append(c)
    args_list = []
    while True:
        if not line:
            raise ReadError("\")\" was not found")
        c = line.popleft()
        if c == ")":
            break
        elif c == " ":
            continue
        args_list.append(c)
    ope = "".join(ope_list)
    args = "".join(args_list).split(",")
    if ope in reserved:
        pass
    return ope, args, 0
    
        
    
    
    
from lib.base import *
def parser(ope: str, args, ans: list):
    if ope == "":
        return
    if ope == "push":
        push(ans, args)
    elif ope == "copy":
        copy(ans)
    elif ope == "swap":
        swap(ans)
    elif ope == "pop":
        swap(ans)
    elif ope == "add":
        add(ans)
    elif ope == "sub":
        sub(ans)
    elif ope == "mul":
        mul(ans)
    elif ope == "div":
        div(ans)
    elif ope == "mod":
        mod(ans)
    elif ope == "save":
        save(ans)
    elif ope == "load":
        load(ans)
    elif ope == "label":
        label(ans, args)
    elif ope == "jump":
        jump(ans, args)
    elif ope == "zeroJump":
        zeroJump(ans, args)
    elif ope == "lessJump":
        lessJump(ans, args)
    elif ope == "callSub":
        callSub(ans, args)
    elif ope == "endSub":
        endSub(ans)
    elif ope == "printChar":
        printChar(ans)
    elif ope == "printNum":
        printNum(ans)
    elif ope == "readChar":
        readChar(ans)
    elif ope == "readNum":
        readNum(ans)

import sys
file_name = sys.argv[1]
    
with open(file_name, "r") as f:
    ans = []

    read_program(f.read(), ans)    
    
    ans.append(n)
    ans.append(n)
    ans.append(n)
    
    ans.append(n)
    ans.append(n)
    print("".join(ans))