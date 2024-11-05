from lib.base import *
import lib.util as util

def saveTo(ans, args):
    """
    指定したアドレスにスタックの先頭の値を保存する。保存したい値を引数に入れることもできる

    [アドレス, *値]
    """
    if len(args) == 2:
        push(ans, [args[0]])
        push(ans, [args[1]])
        save(ans)
    elif len(args) == 1:
        push(ans, [args[0]])
        swap(ans)
        save(ans)

def loadFrom(ans, args):
    """
    指定したアドレスから値を読み込みスタックの先頭に追加する。

    [アドレス]
    """
    push(ans, [args[0]])
    load(ans)

def namedSave(ans, args):
    """
    指定した変数名にアドレスを割り当て、そのアドレスにスタックの先頭にある値を保存する。保存したい値は引数に入れることもできる。

    引数の値は変数でもよい

    トランスパイラで変数名とアドレスを対応させている(コンパイル時に決まる)ため、ローカル変数に使用するべきではない。

    また、変数に使われるアドレスは-100番以下のアドレスになる

    [変数名, *値]
    """
    if args[0] not in util.var_to_address:
        address = util.get_next_address()
        util.var_to_address[args[0]] = address
    else:
        address = util.var_to_address[args[0]]
    if len(args) == 1:
        saveTo(ans, [address])
    if len(args) == 2:
        if util.is_digit(args[1]):
            saveTo(ans, [address, args[1]])
        else:
            namedLoad(ans, [args[1]])
            saveTo(ans, [address])

def namedLoad(ans, args):
    """
    指定した変数名に保存されている値をスタックの先頭に追加する

    [変数]
    """
    address = util.var_to_address[args[0]]
    loadFrom(ans, [address])

def pointAdd(ans, args):
    """
    指定したアドレスに保存されている値に指定した数字を足す

    足す数は変数でもよい
    [アドレス, 足す数]
    """
    loadFrom(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    add(ans)
    saveTo(ans, [args[0]])

def pointSub(ans, args):
    """
    指定したアドレスに保存されている値から指定した数字を引く

    引く数は変数でもよい
    [アドレス, 引く数]
    """
    loadFrom(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    sub(ans)
    saveTo(ans, [args[0]])

def pointMul(ans, args):
    """
    指定したアドレスに保存されている値から指定した数字を掛ける

    掛ける数は変数でもよい
    [アドレス, 掛ける数]
    """
    loadFrom(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    mul(ans)
    saveTo(ans, [args[0]])

def namedAdd(ans, args):
    """
    指定した変数に指定した数字を足す

    足す数は変数でもよい

    [変数, 足す数]
    """
    namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    add(ans)
    namedSave(ans, [args[0]])

def namedSub(ans, args):
    """
    指定した変数に指定した数字を足す

    引く数は変数でもよい

    [変数, 引く数]
    """
    namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    sub(ans)
    namedSave(ans, [args[0]])

def namedMul(ans, args):
    """
    指定した変数に指定した数字を足す

    掛ける数は変数でもよい

    [変数, 掛ける数]
    """
    namedLoad(ans, [args[0]])
    if util.is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    mul(ans)
    namedSave(ans, [args[0]])

def getLocalAddress(ans, args):
    """
    引数で指定した個数分アドレスを確保し、最小のアドレスをスタックの先頭に追加する。

    使われるアドレスは100番以上になる。

    どのアドレスまで使われたかを-10番に保存している
    """
    loadFrom(ans, [-10])
    pointAdd(ans, [-10, args[0]])


def eval(ans, args):
    """
    引数を評価し、満たすなら1を、満たさないなら0をスタックの先頭に追加する

    v1, v2は数値または変数

    operatorは =, >, <, !=のどれかである

    [v1, operator, v2]
    """


