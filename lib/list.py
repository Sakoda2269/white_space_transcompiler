from lib.base import *
from lib.advanced import *
import lib.util as util

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
        address = util.get_next_address(int(size) + 1)
        namedSave(ans, [var, address])
        saveTo(ans, [address, 0])

    elif len(args) == 4:
        var, size, itype, init = args
        address = util.get_next_address(int(size) + 1)
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
        if util.is_digit(value):
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


