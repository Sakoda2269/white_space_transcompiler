from collections import deque

class ReadError(Exception): ...
class ParseError(Exception): ...
    
t = "\t"
n = "\n"
s = " "

from lib.base import *
from lib.advanced import *
from lib.util import get_next_label
from lib.funcs import *

def my_while(ans, args):
    """
    eval(a1, a2, a3)を満たす間actsを繰り返す

    a1,a3は数値、変数。a2は=, <, >, !=。actsは処理である

    [a1, a2, a3, acts]
    """
    a1, a2, a3, acts = args

func_set = set()
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
    elif ope == "saveTo":
        saveTo(ans, args)
    elif ope == "loadFrom":
        loadFrom(ans, args)
    elif ope == "namedSave":
        namedSave(ans, args)
    elif ope == "namedLoad":
        namedLoad(ans, args)
    elif ope == "pointAdd":
        pointAdd(ans, args)
    elif ope == "pointSub":
        pointSub(ans, args)
    elif ope == "pointMul":
        pointMul(ans, args)
    elif ope == "namedAdd":
        namedAdd(ans, args)
    elif ope == "namedSub":
        namedSub(ans, args)
    elif ope == "namedMul":
        namedMul(ans, args)
    elif ope == "getLocalAddress":
        getLocalAddress(ans, args)
    elif ope == "isEq":
        callIsEq(ans, args, func_set)
    elif ope == "isGt":
        callIsGt(ans, args, func_set)
    elif ope == "isLt":
        callIsLt(ans, args, func_set)
    elif ope == "isLtE":
        callIsLtE(ans, args, func_set)
    elif ope == "isGtE":
        callIsGtE(ans, args, func_set)
    else:
        raise ParseError(ope + " is not a function")


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

import sys
file_name = sys.argv[1]
    
with open(file_name, "r") as f:
    ans = []
    saveTo(ans, [-10, 100])
    read_program(f.read(), ans)    
    
    ans.append(n)
    ans.append(n)
    ans.append(n)
    for f in func_set:
        f(ans)
    
    ans.append(n)
    ans.append(n)
    print("".join(ans))