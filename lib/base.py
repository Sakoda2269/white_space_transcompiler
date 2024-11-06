from lib.util import num_to_white

t = "\t"
n = "\n"
s = " "

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
