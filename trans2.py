from collections import deque

class ReadError(Exception): ...
class ParseError(Exception): ...
    
t = "\t"
n = "\n"
s = " "

from lib.base import *
from lib.advanced import *
from lib.util import get_next_label, is_digit
from lib.funcs import *
from lib.list import *

func_set = set()


def my_while(ans, args):
    """
    [a1, a2, a3, acts]

    eval(a1, a2, a3)を満たす間actsを繰り返す

    a1,a3は数値、変数。a2は=, <, >, !=。actsは処理である
    """
    a1, a2, a3, acts = args
    label1 = get_next_label()
    label2 = get_next_label()
    label(ans, [label1])
    eval(ans, [a1, a2, a3], func_set)
    zeroJump(ans, [label2])
    for a in acts:
        parser(a[0], a[1], ans)
    jump(ans, [label1])
    label(ans, [label2])

def my_for(ans, args):
    """
    [var, start, operator, end, step, acts]

    varの初期値をstartとして、eval(var, operator, end)を満たすまでvar += stepをし、actsを実行する

    start, end, step数値でも変数でもよい
    """
    var, start, operator, end, step, acts = args
    if is_digit(start):
        push(ans, [start])
    else:
        namedLoad(ans, [start])
    namedSave(ans, [var])
    label1 = get_next_label()
    label2 = get_next_label()
    label(ans, [label1])
    eval(ans, [var, operator, end], func_set)
    zeroJump(ans, [label2])
    for a in acts:
        parser(a[0], a[1], ans)
    namedAdd(ans, [var, step])
    jump(ans, [label1])
    label(ans, [label2])

def ok(ans, args):
    """
    [v1, operator, v2, acts]

    eval(v1, operator, v2)を満たすならactsを実行する
    """
    v1, operator, v2, acts = args
    label1 = get_next_label()
    eval(ans, [v1, operator, v2], func_set)
    zeroJump(ans, [label1])
    for a in acts:
        parser(a[0], a[1], ans)
    label(ans, [label1])

def ng(ans, args):
    """
    [v1, operator, v2, acts]

    eval(v1, operator, v2)を満たさないならactsを実行する
    """
    v1, operator, v2, acts = args
    label1 = get_next_label()
    eval(ans, [v1, operator, v2], func_set)
    rev(ans)
    zeroJump(ans, [label1])
    for a in acts:
        parser(a[0], a[1], ans)
    label(ans, [label1])

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
        pop(ans)
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
    elif ope == "writeChar":
        writeChar(ans)
    elif ope == "writeNum":
        writeNum(ans)
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
    elif ope == "sAdd":
        sAdd(ans, args)
    elif ope == "sSub":
        sSub(ans, args)
    elif ope == "sMul":
        sMul(ans, args)
    elif ope == "endl":
        endl(ans)
    elif ope == "printNuml":
        printNuml(ans, args)
    elif ope == "printChar":
        printChar(ans, args)
    elif ope == "eval":
        eval(ans, args, func_set)
    elif ope == "evalJump":
        evalJump(ans, args, func_set)
    elif ope == "getLocalAddress":
        getLocalAddress(ans, args)
    elif ope == "while":
        my_while(ans, args)
    elif ope == "for":
        my_for(ans, args)
    elif ope == "ok":
        ok(ans, args)
    elif ope == "ng":
        ng(ans, args)
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
    elif ope == "isNotEq":
        callIsNotEq(ans, args, func_set)
    elif ope == "nextInt":
        callNextInt(ans, args, func_set)
    elif ope == "createList":
        createList(ans, args)
    elif ope == "pushToList":
        pustToList(ans, args)
    elif ope == "getFromList":
        getFromList(ans, args)
    elif ope == "getListSize":
        getListSize(ans, args)
    elif ope == "popFromList":
        popFormList(ans, args)
    else:
        raise ParseError(ope + " is not a function")


def read_program(lines_in: str, ans: list):
    lines = deque(map(lambda x: x + "\n", lines_in.split("\n")))
    while lines:
        l = lines.popleft()
        o, a, s = read_line(l)
        if s == 1:
            tmp = []
            while True:
                l2 = lines.popleft()
                ot, at, st = read_line(l2)
                tmp.append([ot, at])
                if st == 2:
                    break
            a.append(tmp)
            parser(o, a, ans)
        if s == 0:
            parser(o, a, ans)
        

reserved = {"for", "while", "if", "ok", "ng"}

def read_line(line_in: str):
    if not line_in:
        return "", [], -1
    if len(line_in) == 0:
        return "", [], -1
    line = deque(line_in)
    if line[0] == "\n":
        return "", [], -1
    if line[0] == " ":
        line.popleft()
    if line[0] == "}":
        return "", [], 2
    ope_list = []
    while True:
        if not line:
            raise ReadError("\"(\" was not found")
        c = line.popleft()
        if c == "(":
            break
        elif c == " ":
            continue
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
        return ope, args, 1
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
    while func_set:
        func_set.pop()(ans)
    
    ans.append(n)
    ans.append(n)
    print("".join(ans))