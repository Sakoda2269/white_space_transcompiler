t = "\t"
n = "\n"
s = " "

def num_to_white(numstr: str):
    """
    引数で指定した数字をWhitespaceの数字に変換し、それを返す
    """
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

var_address = -100
var_to_address = {}
def get_next_address(extra = 1):
    """
    extraで指定した分だけアドレスを確保し、確保した最小のアドレスを返す。

    例) extra=3の場合

    -103, -104, -105が確保され、-105を返す    
    """
    global var_address
    for i in range(extra):
        var_address -= 1
    return var_address

def is_digit(num):
    """
    numが数値ならばTrueを、そうでないならFalseを返す
    """
    try:
        int(num)
    except Exception:
        return False
    return True

next_label = -100
def get_next_label():
    """
    使用していないラベル番号を取得する
    
    ラベル番号は-100番以下になる
    """
    global next_label
    tmp = next_label
    next_label -= 1
    return tmp
    
def get_text(s):
    ans = []
    flg = False
    for c in s:
        if flg:
            if c == "\"":
                break
            ans.append(c)
        else:
            if c == "\"":
                flg = True
    return "".join(ans)
