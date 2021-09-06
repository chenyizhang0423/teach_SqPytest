# 这个模块有前置条件，先登录获取cookie
from config import HOST
import json,requests
from lib.apiLib.login import Login
import pprint


class Lesson:
    def __init__(self,sessionId):
        self.cookie = {"sessionid":sessionId}
        self.url = f'{HOST}/api/mgr/sq_mgr/'
    # 1：课程-新增
    def lesson_add(self,inBody):
        # data要求是JSON格式，此处data是从Excel读取得来的，本身就是字符串所以此处inData不用加双引号。如果是自己写的，则需要加上引号
        payload = {
            'action':'add_course',
            'data':inBody
        }
        reps = requests.post(self.url,data=payload,cookies = self.cookie)
        reps.encoding="unicode_escape"
        return reps.json()
# 新增课程
# testData = '''{"name":"初中化学","desc":"初中化学课程","display_idx":"4"}'''
# sessionid=Login().login(json.dumps({"username":"auto","password":"sdfsdfsdf"}))
# print(sessionid)
# print(Lesson(sessionid).lesson_add(testData))



    # 2: 课程-列出
    def lesson_list(self,inBody):
        payload = inBody
        reps = requests.get(self.url,params=payload,cookies = self.cookie)
        reps.encoding="unicode_escape"
        return reps.json()
# 列出课程
# get请求，传入的若是字典会直接转换为表单
# testData = {"action":"list_course","pagenum":1,"pagesize":20}
# sessionid=Login().login(json.dumps({"username":"auto","password":"sdfsdfsdf"}))
# reps = Lesson(sessionid).lesson_list(testData)
# pprint.pprint(reps)
# for one in Lesson(sessionid).lesson_list(testData)['retlist']:
#     print(one['id'],type(one['id']))



    # 3：课程-删除
    def lesson_delete(self, inBody,idMode = False):
        if idMode == True:
            payload = {
                "action":"delete_course",
                "id":int(inBody)
            }
        else:
            payload = json.loads(inBody)
        reps = requests.delete(self.url, data=payload, cookies=self.cookie)
        reps.encoding = "unicode_escape"
        return reps.json()
# testData = {"action":"list_course","pagenum":1,"pagesize":20}
# sessionid=Login().login(json.dumps({"username":"auto","password":"sdfsdfsdf"}))
# # 循环课程id，然后直接删除
# for one in Lesson(sessionid).lesson_list(testData)['retlist']:
#     # print(one,one['id'],type(one['id']))
#     Lesson(sessionid).lesson_delete(one['id'])
#
# testData1 = '''{"name":"初中化学","desc":"初中化学课程","display_idx":"4"}'''
# Lesson(sessionid).lesson_add(testData1)



    # 4：课程修改
    def lesson_modify(self,inBody):
        payload = {
            "action":"modify_course",
            "id":int(inBody),
            "newdata":'''
                    {
                    "name":"初中化学666",
                    "desc":"初中化学课程",
                    "display_idx":"4"
                        }'''
        }
        reps = requests.put(self.url,json=payload,cookies = self.cookie)
        reps.encoding="unicode_escape"
        return reps.json()


# testData = {"action":"list_course","pagenum":1,"pagesize":20}
# sessionid=Login().login(json.dumps({"username":"auto","password":"sdfsdfsdf"}))
# # 循环课程id，然后直接修改
# for one in Lesson(sessionid).lesson_list(testData)['retlist']:
#     print(one,one['id'],type(one['id']))
#     Lesson(sessionid).lesson_modify(one['id'])



# get请求，传入的若是字典会直接转换为表单
# testData = {"action":"list_course","pagenum":1,"pagesize":20}
# sessionid=Login().login(json.dumps({"username":"auto","password":"sdfsdfsdf"}))
# reps = Lesson(sessionid).lesson_list(testData)
# pprint.pprint(reps)