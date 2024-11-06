
from lib.base import *
from lib.advanced import *
import lib.util as util

def callIsEq(ans, args, funcs):
    """
    第一引数と第二引数が等しければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    funcs.add(isEq)
    if util.is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [100])

def callIsNotEq(ans, args, funcs):
    """
    第一引数と第二引数が等しくなければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsEq(ans, args, funcs)
    rev(ans)

def isEq(ans):
    """
    第一引数と第二引数が等しければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    label(ans, [100])
    label1 = util.get_next_label()
    label2 = util.get_next_label()
    sub(ans)
    zeroJump(ans, [label1])
    push(ans, [0])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])
    endSub(ans)

def callIsGt(ans, args, funcs):
    """
    第一引数>第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    funcs.add(isGt)
    if util.is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [101])

def isGt(ans):
    label1 = util.get_next_label()
    label2 = util.get_next_label()
    label(ans, [101])
    swap(ans)
    sub(ans)
    lessJump(ans, [label1])
    push(ans, [0])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])
    endSub(ans)

def callIsLt(ans, args, funcs):
    """
    第一引数<第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsGt(ans, [args[1], args[0]], funcs)

def callIsGtE(ans, args, funcs):
    """
    第一引数>=第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    funcs.add(isGtE)
    if util.is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [102])

def isGtE(ans):
    label1 = util.get_next_label()
    label2 = util.get_next_label()
    label(ans, [102])
    sub(ans)
    lessJump(ans, [label1])
    push(ans, [1])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [0])
    label(ans, [label2])
    endSub(ans)

def callIsLtE(ans, args, funcs):
    """
    第一引数<=第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsGtE(ans, [args[1], args[0]], funcs)

def callNextInt(ans, args, funcs):
    """
    [*変数~]

    空白または改行まで数値を読み取る

    変数を入れた場合、その順番に変数に保存する。

    好きなだけ変数を入れることができる。
    """
    funcs.add(nextInt)
    callSub(ans, [103])
    if args[0] != "":
        namedSave(ans, [args[0]])
        for i in range(len(args) - 1):
            callSub(ans, [103])
            namedSave(ans, [args[i + 1]])            

def nextInt(ans):
    from trans2 import my_while
    label1 = util.get_next_label()
    label(ans, [103])
    push(ans, [0])#
    my_while(ans, [1, "=", 1, [
        ["push", ["-1"]],
        ["readChar", []],##
        ["loadFrom", ["-1"]],
        ["copy", []],###
        ["sSub", ["10"]],###
        ["zeroJump", [label1]],##
        ["copy", []],###
        ["sSub", ["32"]],###
        ["zeroJump", [label1]],##
        ["sSub", ["48"]],##
        ["swap", []],##
        ["sMul", ["10"]],##
        ["add", []],#
    ]])
    label(ans, [label1])
    pop(ans)
    endSub(ans)
    