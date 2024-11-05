
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
    callIsGt(ans, [args[0], args[1]], funcs)

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
    