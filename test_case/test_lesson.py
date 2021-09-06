import pytest,requests
from lib.apiLib.login import Login
from lib.apiLib.lesson import Lesson
import json
from tools.excelMethod import get_excelData,set_excelData
import os


# @pytest.fixture(scope="function")
# def lesson_delete_fixture():
#     #1: 登录
#     session = Login().login('{"username":"auto","password":"sdfsdfsdf"}',False)
#     #2：列出课程
#     testData = {"action": "list_course", "pagenum": 1, "pagesize": 20}
#     lessonList = Lesson(session).lesson_list(testData)['retlist']
#     #3：删除课程
#     for lesson in lessonList:
#         Lesson(session).lesson_delete(lesson['id'])

@pytest.mark.lesson
@pytest.mark.usefixtures('lesson_delete_fixture_class')
# 课程模块测试类
class TestLesson:
    loginData = Login().login('{"username":"auto","password":"sdfsdfsdf123"}',True)
    print(loginData)
    def setup_class(self):
        print("----类级别，只要调用测试类，这个就第一个执行")
        self.sessionid = Login().login('{"username":"auto","password":"sdfsdfsdf"}')
        #print(self.sessionid)

    @pytest.mark.skipif(loginData !=0,reason = "登陆失败")
    #@pytest.mark.skip("无条件跳过")
    @pytest.mark.lesson_add
    # 1: 课程新增
    @pytest.mark.parametrize('body,resData', get_excelData("2-课程模块", 2, 26))
    def test_lesson_add(self,body,resData):
        res = Lesson(self.sessionid).lesson_add(body)
        print(res)
        print(resData,json.loads(resData)['retcode'])
        assert res["retcode"] == json.loads(resData)['retcode']

    @pytest.mark.skipif(loginData != 0, reason="登陆失败")
    #@pytest.mark.skipif(1==2,reason="需要满足前面的条件，才会跳过该测试该方法的执行")
    @pytest.mark.lesson_list
    @pytest.mark.usefixtures('lesson_add_fixture')
    @pytest.mark.parametrize('body,resData', get_excelData("2-课程模块", 27, 38))
    # 2: 课程-列出
    def test_lesson_list(self,body,resData):
        res = Lesson(self.sessionid).lesson_list(json.loads(body))
        assert res["retcode"] == json.loads(resData)['retcode']


    @pytest.mark.lesson_delete
    @pytest.mark.usefixtures('lesson_add_fixture')
    @pytest.mark.parametrize('body,resData', get_excelData("2-课程模块", 39, 46))
    # 3: 课程-删除
    def test_lesson_delete(self,body,resData,idMode = False):
        res = Lesson(self.sessionid).lesson_delete(body)
        assert res["retcode"] == json.loads(resData)['retcode']


if __name__ == '__main__':
    #pytest.main(['test_lesson.py','-s','--alluredir','../report/tmp'])
    # 定制化执行，只指令lesson_add标签下的用例。如果执行多个，用or， pytest.main(['test_lesson.py', '-s','-m','lesson_add or lesson_list'])
    #pytest.main(['test_lesson.py', '-s','-m','lesson_add'])
    # 排除法运行, 执行除lesson_add,lesson_list以外的用例
    #pytest.main(['test_lesson.py', '-s', 'not (lesson_add or lesson_list)'])

    pytest.main(['test_lesson.py', '-s','--alluredir','../report/tmp'])
    # 方案1：直接生成报告
    # os.system('allure generate ../report/tmp -o ../report/loginReport --clean')
    # 方案2： 直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')

