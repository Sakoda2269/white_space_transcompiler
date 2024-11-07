from collections import deque
from lib.util import *

class ReadError(Exception): ...
class ParseError(Exception): ...
    
t = "\t"
n = "\n"
s = " "


func_set = set()


def push(ans, args):
    """
    スタックの先頭にに数字を追加する

    [追加したい数字]
    """
    ans.append(s)
    ans.append(s)
    ans.append(num_to_white(args[0]))

def copy(ans):
    """
    スタックの先頭を複製する

    []
    """
    ans.append(s)
    ans.append(n)
    ans.append(s)

def swap(ans):
    """
    スタックの先頭をと先頭から2番目を入れ替える

    []
    """
    ans.append(s)
    ans.append(n)
    ans.append(t)

def pop(ans):
    """
    スタックの先頭を削除する

    []
    """
    ans.append(s)
    ans.append(n)
    ans.append(n)

def add(ans):
    """
    スタックの 二番目 + 先頭 を計算し、スタックの先頭に追加する

    []
    """
    ans.append(t)
    ans.append(s)
    ans.append(s)
    ans.append(s)

def sub(ans):
    """
    スタックの 二番目 - 先頭 を計算し、スタックの先頭に追加する

    []
    """
    ans.append(t)
    ans.append(s)
    ans.append(s)
    ans.append(t)

def mul(ans):
    """
    スタックの 二番目 * 先頭 を計算し、スタックの先頭に追加する

    []
    """
    ans.append(t)
    ans.append(s)
    ans.append(s)
    ans.append(n)

def div(ans):
    """
    スタックの 二番目 / 先頭 を計算し、スタックの先頭に追加する

    []
    """
    ans.append(t)
    ans.append(s)
    ans.append(t)
    ans.append(s)

def mod(ans):
    """
    スタックの 二番目 % 先頭 を計算し、スタックの先頭に追加する（二番目が負の数だと負の数になる）

    []
    """
    ans.append(t)
    ans.append(s)
    ans.append(t)
    ans.append(t)

def save(ans):
    """
    スタックの先頭を二番目が指すアドレスに保存する

    []
    """
    ans.append(t)
    ans.append(t)
    ans.append(s)

def load(ans):
    """
    スタックの先頭が指すアドレスから数を取得し、スタックの先頭に追加する

    []
    """
    ans.append(t)
    ans.append(t)
    ans.append(t)

def label(ans, args):
    """
    プログラムにラベルを張る

    [ラベル番号]
    """
    ans.append(n)
    ans.append(s)
    ans.append(s)
    ans.append(num_to_white(args[0]))

def jump(ans, args):
    """
    指定したラベルに移動する

    [ラベル番号]
    """
    ans.append(n)
    ans.append(s)
    ans.append(n)
    ans.append(num_to_white(args[0]))

def zeroJump(ans, args):
    """
    スタックの先頭が0ならば、指定したラベルに移動する

    [ラベル番号]
    """
    ans.append(n)
    ans.append(t)
    ans.append(s)
    ans.append(num_to_white(args[0]))

def lessJump(ans, args):
    """
    スタックの先頭が負ならば、指定したラベルに移動する

    [ラベル番号]
    """
    ans.append(n)
    ans.append(t)
    ans.append(t)
    ans.append(num_to_white(args[0]))

def callSub(ans, args):
    """
    指定したラベルをサブルーチンとして呼び出す

    [ラベル番号]
    """
    ans.append(n)
    ans.append(s)
    ans.append(t)
    ans.append(num_to_white(args[0]))

def endSub(ans):
    """
    サブルーチンを終了する

    []
    """
    ans.append(n)
    ans.append(t)
    ans.append(n)

def writeChar(ans):
    """
    スタックの先頭を文字として出力する

    []
    """
    ans.append(t)
    ans.append(n)
    ans.append(s)
    ans.append(s)

def writeNum(ans):
    """
    スタックの先頭を数字として出力する

    []
    """
    ans.append(t)
    ans.append(n)
    ans.append(s)
    ans.append(t)

def readChar(ans):
    """
    標準入力から一文字読み取り、スタックの先頭が指すアドレスへ保存する

    []
    """
    ans.append(t)
    ans.append(n)
    ans.append(t)
    ans.append(s)

def readNum(ans):
    """
    標準入力から改行まで数字を読み取り、スタックの先頭が指すアドレスへ保存する(空白区切りではない)
    
    []
    """
    ans.append(t)
    ans.append(n)
    ans.append(t)
    ans.append(t)


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
    if args[0] not in var_to_address:
        address = get_next_address()
        var_to_address[args[0]] = address
    else:
        address = var_to_address[args[0]]
    if len(args) == 1:
        saveTo(ans, [address])
    if len(args) == 2:
        if is_digit(args[1]):
            saveTo(ans, [address, args[1]])
        else:
            namedLoad(ans, [args[1]])
            saveTo(ans, [address])

def namedLoad(ans, args):
    """
    指定した変数名に保存されている値をスタックの先頭に追加する

    [変数]
    """
    address = var_to_address[args[0]]
    loadFrom(ans, [address])

def pointAdd(ans, args):
    """
    指定したアドレスに保存されている値に指定した数字を足す

    足す数は変数でもよい
    [アドレス, 足す数]
    """
    loadFrom(ans, [args[0]])
    if is_digit(args[1]):
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
    if is_digit(args[1]):
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
    if is_digit(args[1]):
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
    if is_digit(args[1]):
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
    if is_digit(args[1]):
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
    if is_digit(args[1]):
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

def sAdd(ans, args):
    """
    スタックの先頭に引数で指定した数字を足す

    足す数は変数でもよい
    """
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    add(ans)

def sSub(ans, args):
    """
    スタックの先頭に引数で指定した数字を引く

    引く数は変数でもよい
    """
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    sub(ans)

def sMul(ans, args):
    """
    スタックの先頭に引数で指定した数字を掛ける

    掛ける数は変数でもよい
    """
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    mul(ans)

def rev(ans):
    """
    スタックの先頭が0ならば1に、1ならば0にする
    """
    sSub(ans, [1])
    sMul(ans, [-1])

def endl(ans):
    """
    改行を出力する

    []
    """
    push(ans, [ord("\n")])
    writeChar(ans)

def printNuml(ans, args):
    """
    指定した数値を改行付きで出力する。指定しない場合はスタックのを数値として解釈し出力する。

    数値は変数でもよい

    [*数値]
    """
    if args[0] == "":
        pass
    elif is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    writeNum(ans)
    endl(ans)

def printChar(ans, args):
    """
    指定した文字を出力する

    ダブルクォーテーションで囲んでいない場合は変数と認識され、保存してあるものを文字と解釈し出力する

    [文字]
    """
    if args[0][0] == "\"":
        s = get_text(args[0])
        push(ans, [ord(s)])
    else:
        namedLoad(ans, [args[0]])
    writeChar(ans)

def eval(ans, args):
    """
    引数を評価し、満たすなら1を、満たさないなら0をスタックの先頭に追加する

    v1, v2は数値または変数

    operatorは =, >, >=, <=, <, !=のどれかである

    [v1, operator, v2]
    """
    v1, ope, v2 = args
    if ope == "=":
        callIsEq(ans, [v1, v2])
    elif ope == ">":
        callIsGt(ans, [v1, v2])
    elif ope == ">=":
        callIsGtE(ans, [v1, v2])
    elif ope == "<":
        callIsLt(ans, [v1, v2])
    elif ope == "<=":
        callIsLtE(ans, [v1, v2])
    elif ope == "!=":
        callIsNotEq(ans, [v1, v2])

def evalJump(ans, args):
    """
    [v1, operator, v2, oklabel, nglabel]

    eval(v1, operator, v2)を満たすならoklabelへ、満たさないならnglabelへジャンプする
    """

    v1, ope, v2, ok, ng =args
    eval(ans, [v1, ope, v2])
    zeroJump(ans, [ng])
    jump(ans, [ok])


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
    eval(ans, [a1, a2, a3])
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
    eval(ans, [var, operator, end])
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
    eval(ans, [v1, operator, v2])
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
    eval(ans, [v1, operator, v2])
    rev(ans)
    zeroJump(ans, [label1])
    for a in acts:
        parser(a[0], a[1], ans)
    label(ans, [label1])


def callIsEq(ans, args):
    """
    第一引数と第二引数が等しければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    func_set.add(isEq)
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [100])

def callIsNotEq(ans, args):
    """
    第一引数と第二引数が等しくなければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsEq(ans, args)
    rev(ans)

def isEq(ans):
    """
    第一引数と第二引数が等しければ1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    label(ans, [100])
    label1 = get_next_label()
    label2 = get_next_label()
    sub(ans)
    zeroJump(ans, [label1])
    push(ans, [0])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])
    endSub(ans)

def callIsGt(ans, args):
    """
    第一引数>第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    func_set.add(isGt)
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [101])

def isGt(ans):
    label1 = get_next_label()
    label2 = get_next_label()
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

def callIsLt(ans, args):
    """
    第一引数<第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsGt(ans, [args[1], args[0]])

def callIsGtE(ans, args):
    """
    第一引数>=第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    func_set.add(isGtE)
    if is_digit(args[0]):
        push(ans, [args[0]])
    else:
        namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    callSub(ans, [102])

def isGtE(ans):
    label1 = get_next_label()
    label2 = get_next_label()
    label(ans, [102])
    sub(ans)
    lessJump(ans, [label1])
    push(ans, [1])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [0])
    label(ans, [label2])
    endSub(ans)

def callIsLtE(ans, args):
    """
    第一引数<=第二引数ならば1を、そうでなければ0をスタックの先頭に追加する

    引数はどちらも数字でも変数でもよい
    """
    callIsGtE(ans, [args[1], args[0]])

def callNextInt(ans, args):
    """
    [*変数~]

    空白または改行まで数値を読み取る

    変数を入れた場合、その順番に変数に保存する。

    好きなだけ変数を入れることができる。
    """
    func_set.add(nextInt)
    callSub(ans, [103])
    if args[0] != "":
        namedSave(ans, [args[0]])
        for i in range(len(args) - 1):
            callSub(ans, [103])
            namedSave(ans, [args[i + 1]])            

def nextInt(ans):
    label1 = get_next_label()
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
    

def createList(ans, args):
    """
    [変数名, 最大サイズ, *初期値の型, *初期値]

    リストを作成し、変数名に先頭アドレスを保存する。

    先頭アドレスには要素数を保存している

    最大サイズを超えて要素を追加してはいけない。

    最大サイズを変数にすることはできない
    
    初期値を指定するとその初期値で最大サイズ分のリストを作成する

    初期値を指定する場合は初期値の型を指定しなければならない
    """
    if len(args) == 2:
        var, size = args
        address = get_next_address(int(size) + 1)
        namedSave(ans, [var, address])
        saveTo(ans, [address, 0])

    elif len(args) == 4:
        var, size, itype, init = args
        address = get_next_address(int(size) + 1)
        namedSave(ans, [var, address])
        saveTo(ans, [address, int(size)])
        for i in range(int(size)):
            if itype == "int":
                getLocalAddress(ans, [2])
                copy(ans)
                saveTo(ans, [address + i + 1])
                copy(ans)
                push(ans, [1])
                save(ans)
                sAdd(ans, [1])
                push(ans, [init])
                save(ans)

def pustToList(ans, args):
    """
    [list, type, value]

    指定したリストに値を追加する。

    値は変数でもよいが、型は指定すること
    """

    var, itype, value = args
    namedLoad(ans, [var])
    copy(ans)
    load(ans)
    add(ans)
    sAdd(ans, [1])
    if itype == "int":
        getLocalAddress(ans, [2])
        copy(ans)
        push(ans, [1])
        save(ans)
        copy(ans)
        sAdd(ans, [1])
        if is_digit(value):
            push(ans, [value])
        else: 
            namedLoad(ans, [value])
        save(ans)
    save(ans)
    namedLoad(ans, [var])
    load(ans)
    sAdd(ans, [1])
    namedLoad(ans, [var])
    swap(ans)
    save(ans)

def getFromList(ans, args):
    """
    [list, num]

    指定したリストのnum番目の値を取得し、スタックの先頭に追加する

    numは変数でもよい
    """
    namedLoad(ans, [args[0]])
    push(ans, [args[1]])
    add(ans)
    sAdd(ans, [1])
    load(ans)
    sAdd(ans, [1])
    load(ans)

def getListSize(ans, args):
    """
    [list]

    指定したリストの要素数を取得し、スタックの先頭に追加する
    """
    namedLoad(ans, [args[0]])
    load(ans)

def popFormList(ans, args):
    """
    [list]
    
    指定したリストの最後の要素を取得し、リストから削除する
    """
    namedLoad(ans, [args[0]])#
    copy(ans)##
    load(ans)##
    add(ans)#
    load(ans)#
    sAdd(ans, [1])#
    load(ans)#

    namedLoad(ans, [args[0]])##
    load(ans)##
    sSub(ans, [1])##
    namedLoad(ans, [args[0]])###
    swap(ans)###
    save(ans)#

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
        eval(ans, args)
    elif ope == "evalJump":
        evalJump(ans, args)
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
        callIsEq(ans, args)
    elif ope == "isGt":
        callIsGt(ans, args)
    elif ope == "isLt":
        callIsLt(ans, args)
    elif ope == "isLtE":
        callIsLtE(ans, args)
    elif ope == "isGtE":
        callIsGtE(ans, args)
    elif ope == "isNotEq":
        callIsNotEq(ans, args)
    elif ope == "nextInt":
        callNextInt(ans, args)
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

# import sys
# file_name = sys.argv[1]

file_name = "C:\\Users\\takot\\Documents\\Education\\ws\\white_space_transcompiler\\target.txt"
    
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