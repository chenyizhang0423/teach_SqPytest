import requests,hashlib


# hashlib.md5(b"xxxx").hexdigest
def get_md5Data(psw):
    password = f"zr{psw}hg"
    #1: 创建一个MD5对象
    md5 = hashlib.md5()
    #2: 加密， update
    md5.update(password.encode("utf-8"))
    # 输出结果(加密之后得到的是16进制字符串)
    print(md5.hexdigest())
    return md5.hexdigest()