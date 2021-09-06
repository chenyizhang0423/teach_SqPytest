import requests,json
from config import HOST

class Login:
    def login(self,inData,flag=False):
        # url: 考虑可维护性，不要写死
        url = f'{HOST}/api/mgr/loginReq'
        # 请求头   字典类型
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        # 因为直接从Excel中获取到的数据是字符串，而此处要传入的是字典，所以这里直接调用json.loads()方法进行处理，进而得到字典
        payload = json.loads(inData)
        reps = requests.post(url, data=payload)
        # 这个登录接口是后续其他接口的前提条件，所以这里加个flag用于标记，便于后续接口调用时要返回什么。
        if flag == False:
            return reps.cookies["sessionid"]
        else:
            return reps.json()
if __name__ == '__main__':
    reps = Login().login('{"username":"auto","password":"sdfsdfsdf"}',True)
    print(reps)
