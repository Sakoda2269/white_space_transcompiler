from collections import deque

# t = "T"
# n = "\n"
# s = "S"

t = "\t"
n = "\n"
s = " "

used_address = -1000
name_map = {}

used_label = -10000

MAX_NUM = 200000

def get_next_address(extra = 0):
    global used_address
    for i in range(extra):
        used_address -= 1
    used_address -= 1
    next_address = used_address
    return next_address

def get_next_address2(num):
    loadFrom(ans, ["-100"])
    loadFrom(ans, ["-100"])
    sAdd(ans, [num])
    push(ans, ["-100"])
    swap(ans)
    save(ans)

def get_next_label():
    global used_label
    next_label = used_label
    used_label -= 1
    return str(next_label)

def is_digit(num):
    try:
        int(num)
        return True
    except Exception:
        return False

def _get_string(s):
    tmp = s
    tmp2 = []
    flg = False
    for c in tmp:
        if not flg:
            if c == "\"":
                flg = True
            continue
        else:
            if c == "\"":
                break
            tmp2.append(c)
    return "".join(tmp2)

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

def printChar(ans):
    """
    スタックの先頭を文字として出力する

    []
    """
    ans.append(t)
    ans.append(n)
    ans.append(s)
    ans.append(s)

def printNum(ans):
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

def nextChar(ans):
    push(ans, [1])
    readChar(ans)
    push(ans, [1])
    load(ans)

def saveTo(ans, args):
    if len(args) == 1:
        push(ans, args)
        swap(ans)
        save(ans)
    elif len(args) == 2:
        push(ans, [args[1]])
        push(ans, [args[0]])
        save(ans)

def namedSave(ans, args):
    tmp = args[0].replace(" ", "")
    if len(args) == 1:
        if tmp not in name_map:
            name_map[tmp] = get_next_address()
        saveTo(ans, [name_map[tmp]])
    elif len(args) == 2:
        if tmp not in name_map:
            name_map[tmp] = get_next_address()
        saveTo(ans, [args[1], name_map[tmp]])
    
def loadFrom(ans, args):
    push(ans, args)
    load(ans)
    
def namedLoad(ans, args):
    tmp = args[0].replace(" ", "")
    loadFrom(ans, [name_map[tmp]])

def eqJump(ans, args):
    push(ans, [args[0]])
    sub(ans)
    zeroJump(ans, [args[1]])

def charEqJump(ans, args):
    if args[0] == "\\n":
        args[0] = "\n"
    eqJump(ans, [str(ord(args[0])), args[1]])

def pnEqJump(ans, args):
    loadFrom(ans, [args[0]])
    eqJump(ans, args[1:])

def ppEqJump(ans, args):
    loadFrom(ans, [args[0]])
    loadFrom(ans, [args[1]])
    sub(ans)
    zeroJump(ans, [args[2]])

def nnEqJump(ans, args):
    namedLoad(ans, [args[0]])
    namedLoad(ans, [args[1]])
    sub(ans)
    zeroJump(ans, [args[2]])
    
def ltJump(ans, args):
    push(ans, [args[0]])
    sub(ans)
    lessJump(ans, [args[1]])

def pnLtJump(ans, args):
    loadFrom(ans, [args[0]])
    ltJump(ans, args[1:])

def ppLtJump(ans, args):
    loadFrom(ans, [args[0]])
    loadFrom(ans, [args[1]])
    sub(ans)
    lessJump(ans, [args[2]])

def nnLtJump(ans, args):
    namedLoad(ans, [args[0]])
    namedLoad(ans, [args[1]])
    sub(ans)
    lessJump(ans, [args[2]])

def _print(ans, args):
    for a in _get_string(args[0]):
        push(ans, [str(ord(a))])
        printChar(ans)

def printNuml(ans, args):
    if args[0] == "":
        printNum(ans)
        endl(ans)
    else:
        namedLoad(ans, [args[0]])
        printNum(ans)
        endl(ans)

nextInt_used = False

def callNextInt(ans):
    global nextInt_used
    nextInt_used = True
    callSub(ans, [-102])

def nextInt(ans):
    label(ans, [-102])
    push(ans, [0])
    label(ans, [-100])
    nextChar(ans)
    copy(ans)
    charEqJump(ans, [" ", -101])
    copy(ans)
    charEqJump(ans, ["\n", -101])
    swap(ans)
    push(ans, [10])
    mul(ans)
    swap(ans)
    push(ans, [48])
    sub(ans)
    add(ans)
    jump(ans, [-100])
    label(ans, [-101])
    pop(ans)
    endSub(ans)
    
def _for(ans, args):

    v1, v2, v3, v4, acts = args
    if is_digit(v1):
        push(ans, [v1])
    else:
        namedLoad(ans, [v1])
    namedSave(ans, [v4])

    start_label = get_next_label()
    end_label = get_next_label()
    label(ans, [start_label])
    eval(ans, [v4, "<", v2])
    zeroJump(ans, [end_label])
    for a in acts:
        parser(a[0], a[1], ans)
    namedAdd(ans, [v4, v3])
    jump(ans, [start_label])
    label(ans, [end_label])

def listInput(ans, args):
    name_map[args[0]] = get_next_address(int(args[2]))
    _for(ans, [
        "0", args[1], "1", "_i",
        [
            ["push", [str(name_map[args[0]])]],
            ["namedLoad", ["_i"]],
            ["add", []],
            ["push", ["1"]],
            ["add", []],
            ["nextInt", []],
            ["save", []],
        ]
    ])
    namedLoad(ans, [args[1]])
    namedSave(ans, [args[0]])

def getList(ans, args):
    if len(args) == 1:
        namedLoad(ans, [args[0]])
        add(ans)
        push(ans, ["1"])
        add(ans)
        load(ans)
    if len(args) == 2:
        push(ans, [str(name_map[args[0]])])
        if is_digit(args[1]):
            push(ans, [args[1]])
        else:
            namedLoad(ans, [args[1]])
        add(ans)
        push(ans, ["1"])
        add(ans)
        load(ans)

def getListSize(ans, args):
    namedLoad(ans, [args[0]])
    # load(ans)

def setList(ans, args):
    if len(args) == 2:
        namedLoad(ans, [args[0]])
        add(ans)
        push(ans, ["1"]),
        add(ans)
        namedLoad(ans, [args[1]])
        save(ans)
    if len(args) == 3:
        push(ans, [str(name_map[args[0]])])
        namedLoad(ans, [args[1]])
        add(ans)
        push(ans, ["1"]),
        add(ans)
        namedLoad(ans, [args[2]])
        save(ans)

def popList(ans, args):
    namedSub(ans, [args[0], 1])
    getList(ans, [args[0], args[0]])

def printList(ans, args):
    if args[0] == "":
        copy(ans)
        load(ans)
        namedSave(ans, ["__tmp"])
        _for(ans, [
            "0", "__tmp", "1", "_i", [
                ["copy", []],
                ["getList", ["_i"]],
                ["printNum", []],
                ["print", ["\" \""]]
            ]
        ])
        pop(ans)
        endl(ans)
    elif len(args) == 1:
        _for(ans, [
            "0", args[0], "1", "_i", [
                ["getList", [args[0], "_i"]],
                ["printNum", []],
                ["print", ["\" \""]]
            ]
        ])
        endl(ans)


def createList(ans, args):
    """
    リストを作成

    [名前, 最大要素数, *初期値]
    """
    name_map[args[0]] = get_next_address(int(args[1]))
    namedSave(ans, [args[0], "0"])
    if len(args) == 3:
        for i in range(int(args[1])):
            saveTo(ans, [str(args[2]), str(i + 1 + name_map[args[0]])])
        namedSave(ans, [args[0], args[1]])

def pushToList(ans, args):
    if len(args) == 1:
        getAddress(ans, [args[0]])
        namedLoad(ans, [args[0]])
        add(ans)
        push(ans, ["1"])
        add(ans)
        swap(ans)
        save(ans)
        namedLoad(ans, [args[0]])
        push(ans, ["1"])
        add(ans)
        namedSave(ans, [args[0]])
    if len(args) == 2:
        getAddress(ans, [args[0]])
        namedLoad(ans, [args[0]])
        add(ans)
        push(ans, ["1"])
        add(ans)
        if is_digit(args[1]):
            push(ans, [args[1]])
        else:
            namedLoad(ans, [args[1]])
        save(ans)
        namedLoad(ans, [args[0]])
        push(ans, ["1"])
        add(ans)
        namedSave(ans, [args[0]])


def nextString(ans, args):
    name_map[args[0]] = get_next_address(int(args[1]))
    label1 = get_next_label()
    label2 = get_next_label()
    push(ans, [name_map[args[0]]])
    label(ans, [label1])
    push(ans, [1])
    add(ans)
    copy(ans)
    nextChar(ans)
    copy(ans)
    charEqJump(ans, ["\n", label2])
    save(ans)
    jump(ans, [label1])
    label(ans, [label2])
    pop(ans)
    pop(ans)
    push(ans, [name_map[args[0]]])
    sub(ans)
    push(ans, ["1"])
    sub(ans)
    push(ans, [name_map[args[0]]])
    swap(ans)
    save(ans)

def putString(ans, args):
    s = _get_string(args[1])
    name_map[args[0]] = get_next_address(len(s))
    namedSave(ans, [args[0], str(len(s))])
    for i, c in enumerate(s):
        saveTo(ans, [ord(c), str(name_map[args[0]] + 1 + i)])
    
def charAt(ans, args):
    if len(args) == 1:
        namedLoad(ans, [args[0]])
        push(ans, ["1"])
        add(ans)
        add(ans)
        load(ans)
    if len(args) == 2:
        push(ans, [name_map[args[0]]])
        namedLoad(ans, [args[1]])
        push(ans, ["1"])
        add(ans)
        add(ans)
        load(ans)

def itrNotEqJump(ans, args):
    go_label = args[2]
    label1 = get_next_label()
    namedLoad(ans, [args[0]])
    push(ans, ["1"])
    add(ans)
    namedSave(ans, ["__tmp"])
    _for(ans, [
        "0", "__tmp", "1", "_i", [
            ["getAddress", [args[0]]],
            ["namedLoad", ["_i"]],
            ["add", []],
            ["load", []],
            ["getAddress", [args[1]]],
            ["namedLoad", ["_i"]],
            ["add", []],
            ["load", []],
            ["sub", []],
            ["zeroJump", [str(label1)]],
            ["jump", [str(go_label)]],
            ["label", [str(label1)]],
            ["namedLoad", ["_i"]],
        ]
    ])

def getAddress(ans, args):
    push(ans, [name_map[args[0]]])

def printString(ans, args):
    if args[0] == "":
        copy(ans)
        load(ans)
        namedSave(ans, ["__tmp"])
        _for(ans, [
            "0", "__tmp", "1", "_i",[
                ["copy", []],
                ["push", ["1"]],
                ["namedLoad", ["_i"]],
                ["add", []],
                ["add", []],
                ["load", []],
                ["printChar", []]
            ]
        ])
        pop(ans)
        endl(ans)
    
    elif len(args) == 1:
        _for(ans, [
            "0", args[0], "1", "_i",[
                ["getAddress", [args[0]]],
                ["push", ["1"]],
                ["namedLoad", ["_i"]],
                ["add", []],
                ["add", []],
                ["load", []],
                ["printChar", []]
            ]
        ])
        endl(ans)

def isLt(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    sub(ans)
    lessJump(ans, [label1])

    push(ans, [0])
    jump(ans, [label2])

    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])

def isGt(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    swap(ans)
    sub(ans)
    lessJump(ans, [label1])

    push(ans, [0])
    jump(ans, [label2])

    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])

def isEq(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    namedLoad(ans, [args[0]])
    if is_digit(args[1]):
        push(ans, [args[1]])
    else:
        namedLoad(ans, [args[1]])
    sub(ans)
    zeroJump(ans, [label1])
    push(ans, [0])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [1])
    label(ans, [label2])

def itrEq(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    itrNotEqJump(ans, [args[0], args[1], label1])
    push(ans, [1])
    jump(ans, [label2])
    label(ans, [label1])
    push(ans, [0])
    label(ans, [label2])

def eval(ans, args):
    v1, op, v2 = args
    if op == "=":
        isEq(ans, [v1, v2])
    elif op == "!=":
        isEq(ans, [v1, v2])
        sSub(ans, [1])
        sMul(ans, [-1])
    elif op == "<":
        isLt(ans, [v1, v2])
    elif op == ">":
        isGt(ans, [v1, v2])
    elif op == "i=":
        itrEq(ans, [v1, v2])
    else:
        return

def _if(ans, args):
    v1, op, v2, acts = args
    ok = []
    ng = []
    for a in acts:
        if a[0] == "ok":
            ok = a[1][1]
        elif a[0] == "ng":
            ng = a[1][1]
    label1 = get_next_label()
    label2 = get_next_label()
    eval(ans, [v1, op, v2])
    zeroJump(ans, [label1])
    for a in ok:
        parser(a[0], a[1], ans)
    jump(ans, [label2])
    label(ans, [label1])
    for a in ng:
        parser(a[0], a[1], ans)
    label(ans, [label2])

def _max(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    eval(ans, [args[0], ">", args[1]])
    zeroJump(ans, [label1])
    namedLoad(ans, [args[0]])
    jump(ans, [label2])
    label(ans, [label1])
    namedLoad(ans, [args[1]])
    label(ans, [label2])

def _min(ans, args):
    label1 = get_next_label()
    label2 = get_next_label()
    eval(ans, [args[0], "<", args[1]])
    zeroJump(ans, [label1])
    namedLoad(ans, [args[0]])
    jump(ans, [label2])
    label(ans, [label1])
    namedLoad(ans, [args[1]])
    label(ans, [label2])

def _while(ans, args):
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

def namedAdd(ans, args):
    a1, a2 = args
    namedLoad(ans, [a1])
    if is_digit(a2):
        push(ans, [a2])
        add(ans)
        namedSave(ans, [a1])
    else:
        namedLoad(ans, [a2])
        add(ans)
        namedSave(ans, [a1])

def namedSub(ans, args):
    a1, a2 = args
    namedLoad(ans, [a1])
    if is_digit(a2):
        push(ans, [a2])
        sub(ans)
        namedSave(ans, [a1])
    else:
        namedLoad(ans, [a2])
        sub(ans)
        namedSave(ans, [a1])

def namedMul(ans, args):
    a1, a2 = args
    namedLoad(ans, [a1])
    if is_digit(a2):
        push(ans, [a2])
        mul(ans)
        namedSave(ans, [a1])
    else:
        namedLoad(ans, [a2])
        mul(ans)
        namedSave(ans, [a1])

def sAdd(ans, args):
    a = args[0]
    if is_digit(a):
        push(ans, [a])
        add(ans)
    else:
        namedLoad(ans, [a])
        add(ans)

def sSub(ans, args):
    a = args[0]
    if is_digit(a):
        push(ans, [a])
        sub(ans)
    else:
        namedLoad(ans, [a])
        sub(ans)

def sMul(ans, args):
    a = args[0]
    if is_digit(a):
        push(ans, [a])
        mul(ans)
    else:
        namedLoad(ans, [a])
        mul(ans)

def __if(ans, args):
    a1, a2, a3, oks, ngs = args
    _if(ans, [a1, a2, a3, [
        ["ok", [
            "", oks
        ]],
        ["ng", [
            "", ngs
        ]]
    ]])

def test(ans, args):
    namedSave(ans, ["a", 10])
    namedSave(ans, ["b", 15])
    __if(ans, ["a", "<", "b", [
        ["print", ["\"hello\""]]
    ], [
        ["print", ["\"good\""]]
    ]])

AVL_used = False
def AVL(ans, args):
    global AVL_used
    AVL_used = True
    namedSave(ans, [args[0], "-1"])

def rotate_left(ans):
    namedSave(ans, ["_v"])

    namedLoad(ans, ["_v"])
    sAdd(ans, [3])
    load(ans)
    namedSave(ans, ["_u"])
    
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    sSub(ans, [1])
    namedLoad(ans, ["_u"])
    sAdd(ans, [3])
    load(ans)
    namedSave(ans, ["_urch"])
    __if(ans, ["_urch", "=", "-1", [], [
        ["namedLoad", ["_urch"]],
        ["sAdd", [5]],
        ["load", []],
        ["sub", []]
    ]])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [3])
    namedLoad(ans, ["_u"])
    sAdd(ans, [2])
    load(ans)
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [2])
    namedLoad(ans, ["_v"])
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [4])
    load(ans)
    namedSave(ans, ["_ubias"])
    __if(ans, ["_ubias", "=", "-1", [
        ["namedLoad", ["_u"]],
        ["sAdd", ["4"]],
        ["push", ["0"]],
        ["save", []],
        ["namedLoad", ["_v"]],
        ["sAdd", ["4"]],
        ["push", ["0"]],
        ["save", []]
    ], [
        ["namedLoad", ["_u"]],
        ["sAdd", ["4"]],
        ["push", ["1"]],
        ["save", []],
        ["namedLoad", ["_v"]],
        ["sAdd", ["4"]],
        ["push", ["-1"]],
        ["save", []]
    ]])
    namedLoad(ans, ["_u"])

def rotate_right(ans):
    namedSave(ans, ["_v"])

    namedLoad(ans, ["_v"])
    sAdd(ans, [2])
    load(ans)
    namedSave(ans, ["_u"])
    
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    sSub(ans, [1])
    namedLoad(ans, ["_u"])
    sAdd(ans, [2])
    load(ans)
    namedSave(ans, ["_ulch"])
    __if(ans, ["_ulch", "=", "-1", [], [
        ["namedLoad", ["_ulch"]],
        ["sAdd", [5]],
        ["load", []],
        ["sub", []]
    ]])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [2])
    namedLoad(ans, ["_u"])
    sAdd(ans, [3])
    load(ans)
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [3])
    namedLoad(ans, ["_v"])
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [4])
    load(ans)
    namedSave(ans, ["_ubias"])
    __if(ans, ["_ubias", "=", "-1", [
        ["namedLoad", ["_u"]],
        ["sAdd", ["4"]],
        ["push", ["0"]],
        ["save", []],
        ["namedLoad", ["_v"]],
        ["sAdd", ["4"]],
        ["push", ["0"]],
        ["save", []]
    ], [
        ["namedLoad", ["_u"]],
        ["sAdd", ["4"]],
        ["push", ["-1"]],
        ["save", []],
        ["namedLoad", ["_v"]],
        ["sAdd", ["4"]],
        ["push", ["1"]],
        ["save", []]
    ]])
    namedLoad(ans, ["_u"])

def rotateLR(ans):
    namedSave(ans, ["_v"])
    namedLoad(ans, ["_v"])
    sAdd(ans, [2])
    load(ans)
    namedSave(ans, ["_u"])

    namedLoad(ans, ["_u"])
    sAdd(ans, [3])
    load(ans)
    namedSave(ans, ["_t"])

    namedLoad(ans, ["_t"])
    sAdd(ans, [5])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    load(ans)
    sub(ans)
    namedLoad(ans, ["_t"])
    sAdd(ans, [3])
    load(ans)
    namedSave(ans, ["_trch"])
    __if(ans, ["_trch", "=", "-1", [], [
        ["namedLoad", ["_t"]],
        ["sAdd", [3]],
        ["load", []],
        ["sAdd", [5]],
        ["load", []],
        ["add", []]
    ]])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)


    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    load(ans)
    sSub(ans, [1])
    __if(ans, ["_trch", "=", "-1", [], [
        ["namedLoad", ["_t"]],
        ["sAdd", [3]],
        ["load", []],
        ["sAdd", [5]],
        ["load", []],
        ["sub", []]
    ]])
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [3])
    namedLoad(ans, ["_t"])
    sAdd(ans, [2])
    load(ans)
    save(ans)

    namedLoad(ans, ["_t"])
    sAdd(ans, [2])
    namedLoad(ans, ["_u"])
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [2])
    namedLoad(ans, ["_t"])
    sAdd(ans, [3])
    load(ans)
    save(ans)

    namedLoad(ans, ["_t"])
    sAdd(ans, [3])
    namedLoad(ans, ["_v"])
    save(ans)
    namedLoad(ans, ["_t"])

    update_bias_double(ans)
    namedLoad(ans, ["_t"])

def rotateRL(ans):
    namedSave(ans, ["_v"])
    namedLoad(ans, ["_v"])
    sAdd(ans, [3])
    load(ans)
    namedSave(ans, ["_u"])

    namedLoad(ans, ["_u"])
    sAdd(ans, [2])
    load(ans)
    namedSave(ans, ["_t"])

    namedLoad(ans, ["_t"])
    sAdd(ans, [5])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    load(ans)
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    load(ans)
    sub(ans)
    namedLoad(ans, ["_t"])
    sAdd(ans, [2])
    load(ans)
    namedSave(ans, ["_tlch"])
    __if(ans, ["_tlch", "=", "-1", [], [
        ["namedLoad", ["_t"]],
        ["sAdd", [2]],
        ["load", []],
        ["sAdd", [5]],
        ["load", []],
        ["add", []]
    ]])
    namedLoad(ans, ["_v"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    load(ans)
    sSub(ans, [1])
    __if(ans, ["_tlch", "=", "-1", [], [
        ["namedLoad", ["_t"]],
        ["sAdd", [2]],
        ["load", []],
        ["sAdd", [5]],
        ["load", []],
        ["sub", []]
    ]])
    namedLoad(ans, ["_u"])
    sAdd(ans, [5])
    swap(ans)
    save(ans)

    namedLoad(ans, ["_u"])
    sAdd(ans, [2])
    namedLoad(ans, ["_t"])
    sAdd(ans, [3])
    load(ans)
    save(ans)

    namedLoad(ans, ["_t"])
    sAdd(ans, [3])
    namedLoad(ans, ["_u"])
    save(ans)

    namedLoad(ans, ["_v"])
    sAdd(ans, [3])
    namedLoad(ans, ["_t"])
    sAdd(ans, [2])
    load(ans)
    save(ans)

    namedLoad(ans, ["_t"])
    sAdd(ans, [2])
    namedLoad(ans, ["_v"])
    save(ans)

    namedLoad(ans, ["_t"])
    update_bias_double(ans)
    namedLoad(ans, ["_t"])

def update_bias_double(ans):
    label1 = get_next_label()
    label2 = get_next_label()
    label3 = get_next_label()
    namedSave(ans, ["__v"])
    namedLoad(ans, ["__v"])
    sAdd(ans, [4])
    load(ans)
    namedSave(ans, ["__vbias"])
    isEq(ans, ["__vbias", 1])
    sSub(ans, [1])
    zeroJump(ans, [label1])

    isEq(ans, ["__vbias", -1])
    sSub(ans, [1])
    zeroJump(ans, [label2])

    namedLoad(ans, ["__v"])
    sAdd(ans, [3])
    load(ans)
    sAdd(ans, [4])
    push(ans, [0])
    save(ans)
    namedLoad(ans, ["__v"])
    sAdd(ans, [2])
    load(ans)
    sAdd(ans, [4])
    push(ans, [0])
    save(ans)
    jump(ans, [label3])

    label(ans, [label1])
    namedLoad(ans, ["__v"])
    sAdd(ans, [3])
    load(ans)
    sAdd(ans, [4])
    push(ans, [-1])
    save(ans)
    namedLoad(ans, ["__v"])
    sAdd(ans, [2])
    load(ans)
    sAdd(ans, [4])
    push(ans, [0])
    save(ans)
    jump(ans, [label3])

    label(ans, [label2])
    namedLoad(ans, ["__v"])
    sAdd(ans, [3])
    load(ans)
    sAdd(ans, [4])
    push(ans, [0])
    save(ans)
    namedLoad(ans, ["__v"])
    sAdd(ans, [2])
    load(ans)
    sAdd(ans, [4])
    push(ans, [1])
    save(ans)
    jump(ans, [label3])

    label(ans, [label3])
    namedLoad(ans, ["__v"])
    sAdd(ans, [4])
    push(ans, [0])
    save(ans)

def callInsertAVL(ans, args):
    root, key, value = args
    get_next_address2(6)
    getAddress(ans, [root])
    if is_digit(key):
        push(ans, [key])
    else:
        namedLoad(ans, [key])
    if is_digit(value):
        push(ans, [value])
    else:
        namedLoad(ans, [value])
    callSub(ans, [-200])

def insertAVL(ans):
    label(ans, [-200])
    namedSave(ans, ["_value"])
    namedSave(ans, ["_key"])
    namedSave(ans, ["_root"])
    namedSave(ans, ["_ra"])
    namedLoad(ans, ["_root"])
    load(ans)
    namedSave(ans, ["_root_value"])
    label1 = str(get_next_label())
    label2 = str(get_next_label())

    namedLoad(ans, ["_ra"])
    namedLoad(ans, ["_key"])
    save(ans)
    namedLoad(ans, ["_ra"])
    sAdd(ans, ["1"])
    namedLoad(ans, ["_value"])
    save(ans)
    namedLoad(ans, ["_ra"])
    sAdd(ans, ["2"])
    push(ans, ["-1"])
    save(ans)
    namedLoad(ans, ["_ra"])
    sAdd(ans, ["3"])
    push(ans, ["-1"])
    save(ans)
    namedLoad(ans, ["_ra"])
    sAdd(ans, ["4"])
    push(ans, ["0"])
    save(ans)
    namedLoad(ans, ["_ra"])
    sAdd(ans, ["5"])
    push(ans, ["1"])
    save(ans)

    isEq(ans, ["_root_value", -1])
    zeroJump(ans, [label2])

    namedLoad(ans, ["_root"])
    namedLoad(ans, ["_ra"])
    save(ans)
    jump(ans, [label1])

    label(ans, [label2])
    namedLoad(ans, ["_root_value"])
    namedSave(ans, ["_v_"])
    createList(ans, ["_his1_", MAX_NUM])
    createList(ans, ["_his2_", MAX_NUM])
    label3 = str(get_next_label())
    label4 = str(get_next_label())
    label5 = str(get_next_label())
    _while(ans, ["_v_", "!=", "-1", [
        ["namedLoad", ["_v_"]],
        ["load", []],
        ["namedSave", ["_vkey_"]],
        ["eval", ["_vkey_", ">", "_key"]],
        ["sSub", ["1"]],
        ["zeroJump", [(label3)]],
        ["eval", ["_vkey_", "<", "_key"]],
        ["sSub", ["1"]],
        ["zeroJump", [label4]],
        ["namedLoad", ["_v_"]],
        ["sAdd", ["1"]],
        ["namedLoad", ["_value"]],
        ["save", []],
        ["jump", [label1]],
        ["label", [label3]],
        ["pushToList", ["_his1_", "_v_"]],
        ["pushToList", ["_his2_", "1"]],
        ["namedLoad", ["_v_"]],
        ["sAdd", ["2"]],
        ["load", []],
        ["namedSave", ["_v_"]],
        ["jump", [label5]],
        ["label", [label4]],
        ["pushToList", ["_his1_", "_v_"]],
        ["pushToList", ["_his2_", "-1"]],
        ["namedLoad", ["_v_"]],
        ["sAdd", ["3"]],
        ["load", []],
        ["namedSave", ["_v_"]],
        ["label", [label5]]
    ]])

    getListSize(ans, ["_his1_"])
    sSub(ans, [1])
    namedSave(ans, ["_size_"])
    getList(ans, ["_his1_", "_size_"])
    namedSave(ans, ["_p_"])
    getList(ans, ["_his2_", "_size_"])
    namedSave(ans, ["_pdir_"])

    label6 = get_next_label()
    label7 = get_next_label()

    eval(ans, ["_pdir_", "=", "1"])
    zeroJump(ans, [label6])
    namedLoad(ans, ["_p_"])
    sAdd(ans, [2])
    namedLoad(ans, ["_ra"])
    save(ans)
    jump(ans, [label7])

    label(ans, [label6])
    namedLoad(ans, ["_p_"])
    sAdd(ans, [3])
    namedLoad(ans, ["_ra"])
    save(ans)
    label(ans, [label7])

    label8 = get_next_label()
    _while(ans, ["_his1_", ">", "0", [
        ["popList", ["_his1_"]],
        ["namedSave", ["_v_"]],
        ["popList", ["_his2_"]],
        ["namedSave", ["_dire_"]],

        ["namedLoad", ["_v_"]],
        ["sAdd", ["4"]],
        ["load", []],
        ["sAdd", ["_dire_"]],
        ["namedLoad", ["_v_"]],
        ["sAdd", ["4"]],
        ["swap", []],
        ["save", []],

        ["namedLoad", ["_v_"]],
        ["sAdd", ["5"]],
        ["load", []],
        ["sAdd", ["1"]], 
        ["namedLoad", ["_v_"]],
        ["sAdd", ["5"]],
        ["swap", []],
        ["save", []],

        ["namedSave", ["_new_v_", "-1"]],

        ["namedLoad", ["_v_"]],
        ["sAdd", ["4"]],
        ["load", []],
        ["namedSave", ["_b_"]],

        ["namedLoad", ["_b_"]],
        ["zeroJump", [label8]],

        ["__if", ["_b_", "=", "2", [
            ["namedLoad", ["_v_"]],
            ["sAdd", ["2"]],
            ["load", []],
            ["sAdd", ["4"]],
            ["namedSave", ["_ubias_"]],
            ["__if", ["_ubias_", "=", "-1", [
                ["namedLoad", ["_v_"]],
                ["rotateLR", []],
                ["namedSave", ["_new_v_"]]
            ], [
                ["namedLoad", ["_v_"]],
                ["rotate_right", []],
                ["namedSave", ["_new_v_"]]
            ]]],
            ["jump", [label8]]
        ], [
            ["", []]
        ]]],
        ["__if", ["_b_", "=", "-2", [
            ["namedLoad", ["_v_"]],
            ["sAdd", ["3"]],
            ["load", []],
            ["sAdd", ["4"]],
            ["namedSave", ["_ubias_"]],
            ["__if", ["_ubias_", "=", "1", [
                ["namedLoad", ["_v_"]],
                ["rotateRL", []],
                ["namedSave", ["_new_v_"]]
            ], [
                ["namedLoad", ["_v_"]],
                ["rotate_left", []],
                ["namedSave", ["_new_v_"]]
            ]]],
            ["jump", [label8]]
        ], [
            ["", []]
        ]]],
    ]])

    label(ans, [label8])
    __if(ans, ["_new_v_", "!=", "-1", [
        ["__if", ["_his1_", "=", "0", [
            ["namedLoad", ["_root"]],
            ["namedLoad", ["_new_v_"]],
            ["save", []],
            ["jump", [label1]]
        ], [
            ["", []]
        ]]],
        ["popList", ["_his1_"]],
        ["namedSave", ["_p_"]],
        ["popList", ["_his2_"]],
        ["namedSave", ["_pdir_"]],
        ["namedLoad", ["_p_"]],
        ["sAdd", ["5"]],
        ["load", []],
        ["sAdd", ["1"]],
        ["namedLoad", ["_p_"]],
        ["sAdd", ["5"]],
        ["swap", []],
        ["save", []],
        ["__if", ["_pdir_", "=", "1", [
            ["namedLoad", ["_p_"]],
            ["sAdd", ["2"]],
            ["namedLoad", ["_new_v_"]],
            ["save", []]
        ], [
            ["namedLoad", ["_p_"]],
            ["sAdd", ["3"]],
            ["namedLoad", ["_new_v_"]],
            ["save", []]
        ]]]
    ], [
        ["", []]
    ]])


    _while(ans, ["_his1_", ">", "0", [
        ["popList", ["_his1_"]],
        ["namedSave", ["_p_"]],
        ["popList", ["_his2_"]],
        ["namedLoad", ["_p_"]],
        ["sAdd", ["5"]],
        ["load", []],
        ["sAdd", ["1"]],
        ["namedLoad", ["_p_"]],
        ["sAdd", ["5"]],
        ["swap", []],
        ["save", []]
    ]])

    label(ans, [label1])
    endSub(ans)

def callGetAVL(ans, args):
    root, key = args
    namedLoad(ans, [root])
    if is_digit(key):
        push(ans, [key])
    else:
        namedLoad(ans, [key])
    callSub(ans, [-201])

def getAVL(ans):
    label(ans, [-201])
    namedSave(ans, ["_key"])
    namedSave(ans, ["_v"])
    label1 = get_next_label()
    label2 = get_next_label()
    label3 = get_next_label()
    label4 = get_next_label()
    _while(ans, ["_v", "!=", "-1", [
        ["namedLoad", ["_v"]],
        ["load", []],
        ["namedSave", ["_vkey"]],
        ["eval", ["_vkey", ">", "_key"]],
        ["sSub", ["1"]],
        ["zeroJump", [label1]],
        ["eval", ["_vkey", "<", "_key"]],
        ["sSub", ["1"]],
        ["zeroJump", [label2]],
        ["namedLoad", ["_v"]],
        ["sAdd", [1]],
        ["load", []],
        ["jump", [label4]],
        ["label", [label1]],
        ["namedLoad", ["_v"]],
        ["sAdd", ["2"]],
        ["load", []],
        ["namedSave", ["_v"]],
        ["jump", [label3]],
        ["label", [label2]],
        ["namedLoad", ["_v"]],
        ["sAdd", ["3"]],
        ["load", []],
        ["namedSave", ["_v"]],
        ["label", [label3]]
    ]])
    push(ans, [-1])
    label(ans, [label4])
    endSub(ans)

def endl(ans):
    push(ans, [10])
    printChar(ans)
    
def read(f):
    line = deque(f.readline())
    if not line:
        return "", [], -1
    while line[0] == " ":
        line.popleft()
    if line[0] == "\n":
        return "", [], 1
    if line[0] == "}":
        return "", [], 2
    while line[0] == " ":
        line.popleft()
    op = []
    argsl = []
    while True:
        if line[0] == "(":
            break
        op.append(line.popleft())
    line.popleft()
    while True:
        tmp = line.popleft()
        if tmp == ")":
            break
        argsl.append(tmp)
    ope = "".join(op)
    args = "".join(argsl).split(",")
    if ope == "for" or ope == "if" or ope == "ok" or ope == "ng" or ope == "while":
        tmp = []
        while True:
            o, a, s = read(f)
            if s == 2:
                break
            tmp.append([o, a])
        args.append(tmp)
    return ope, args, 1
    
    

def parser(ope: str, args, ans: list):
    for i in range(len(args)):
        count = 0
        if args[i] == "":
            continue
        if is_digit(args[i]):
            args[i] = str(args[i])
        while args[i][count] == " ":
            count += 1
        args[i] = args[i][count:]
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
    elif ope == "end":
        ans.append(n)
        ans.append(n)
        ans.append(n)
    elif ope == "nextChar":
        nextChar(ans)
    elif ope == "saveTo":
        saveTo(ans, args)
    elif ope == "loadFrom":
        loadFrom(ans, args)
    elif ope == "eqJump":
        eqJump(ans, args)
    elif ope == "charEqJump":
        charEqJump(ans, args)
    elif ope == "pnEqJump":
        pnEqJump(ans, args)
    elif ope == "ppEqJump":
        ppEqJump(ans, args)
    elif ope == "nnEqJump":
        nnEqJump(ans, args)
    elif ope == "ltJump":
        ltJump(ans, args)
    elif ope == "pnLtJump":
        pnLtJump(ans, args)
    elif ope == "ppLtJump":
        ppLtJump(ans, args)
    elif ope == "print":
        _print(ans, args)
    elif ope == "endl":
        endl(ans)
    elif ope == "nextInt":
        callNextInt(ans)
    elif ope == "namedSave":
        namedSave(ans, args)
    elif ope == "namedLoad":
        namedLoad(ans, args)
    elif ope == "printNuml":
        printNuml(ans, args)
    elif ope == "nnLtJump":
        nnLtJump(ans, args)
    elif ope == "for":
        _for(ans, args)
    elif ope == "listInput":
        listInput(ans, args)
    elif ope == "createList":
        createList(ans, args)
    elif ope == "getList":
        getList(ans, args)
    elif ope == "getListSize":
        getListSize(ans, args)
    elif ope == "setList":
        setList(ans, args)
    elif ope == "popList":
        popList(ans, args)
    elif ope == "pushToList":
        pushToList(ans, args)
    elif ope == "printList":
        printList(ans, args)
    elif ope == "nextString":
        nextString(ans, args)
    elif ope == "putString":
        putString(ans, args)
    elif ope == "charAt":
        charAt(ans, args)
    elif ope == "itrNotEqJump":
        itrNotEqJump(ans, args)
    elif ope == "printString":
        printString(ans, args)
    elif ope == "getAddress":
        getAddress(ans, args)
    elif ope == "isLt":
        isLt(ans, args)
    elif ope == "isGt":
        isGt(ans, args)
    elif ope == "isEq":
        isEq(ans, args)
    elif ope == "itrEq":
        itrEq(ans, args)
    elif ope == "eval":
        eval(ans, args)
    elif ope == "if":
        _if(ans, args)
    elif ope == "__if":
        __if(ans, args)
    elif ope == "max":
        _max(ans, args)
    elif ope == "min":
        _min(ans, args)
    elif ope == "while":
        _while(ans, args)
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
    elif ope =="test":
        test(ans, args)
    elif ope == "AVL":
        AVL(ans, args)
    elif ope == "rotate_left":
        rotate_left(ans)
    elif ope == "rotate_right":
        rotate_right(ans)
    elif ope == "rotateLR":
        rotateLR(ans)
    elif ope == "rotateRL":
        rotateRL(ans)
    elif ope == "insert":
        callInsertAVL(ans, args)
    elif ope == "getAVL":
        callGetAVL(ans, args)
    else:
        ans.append(f"{ope} is not a function")

import sys
file_name = sys.argv[1]
    
with open(file_name, "r") as f:
    ans = []
    saveTo(ans, ["100", "-100"])

    while True:
        ope, args, state = read(f)
        if state == -1:
            break
        parser(ope, args, ans)
        
    
    ans.append(n)
    ans.append(n)
    ans.append(n)
    if nextInt_used:
        nextInt(ans)
    if AVL_used:
        insertAVL(ans)
        getAVL(ans)
    ans.append(n)
    ans.append(n)
    print("".join(ans))
