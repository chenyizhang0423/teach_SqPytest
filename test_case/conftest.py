import json

import pytest
import requests
from lib.apiLib.login import Login
from lib.apiLib.lesson import Lesson

@pytest.fixture(scope="session",autouse=True)
def start_demo(request):
    print("------我是整个包的初始化------")
    def fin():
        print('------测试完整，执行整个包的清除操作------')
    request.addfinalizer(fin)  # 这行代码的意思是当整个包的代码运行完之后，回回调fin()这个函数
"""
1-：对于整个课程模块-class
    初始化：删除所有课程
2-：课程的列出接口
     初始化---新增一部分课程
3-：课程的删除接口
     初始化---新增一部分课程
"""

@pytest.fixture(scope="class")
def lesson_delete_fixture_class():
    #1: 登录
    session = Login().login('{"username":"auto","password":"sdfsdfsdf"}',False)
    #2：列出课程
    testData = {"action": "list_course", "pagenum": 1, "pagesize": 20}
    lessonList = Lesson(session).lesson_list(testData)['retlist']
    #3：删除课程
    for lesson in lessonList:
        Lesson(session).lesson_delete(lesson['id'],idMode=True)
    print("-----lesson_delete_fixture_class----")

@pytest.fixture() #默认scope ='function'
def lesson_add_fixture(request):
    # 1: 登录
    session = Login().login('{"username":"auto","password":"sdfsdfsdf"}', False)
    # 2:新增课程
    for one in range(0,6):
        lessonData ={
                    "name":f"初中化学{one:0>3}",
                    "desc":"初中化学课程",
                    "display_idx":f"{one}"
                    }
        Lesson(session).lesson_add(json.dumps(lessonData))
    print("-----lesson_add_fixture_class----")
    def fin():
        print('------用例执行完，删除用例------')
        # 2：列出课程
        testData = {"action": "list_course", "pagenum": 1, "pagesize": 20}
        lessonList = Lesson(session).lesson_list(testData)['retlist']
        # 3：删除课程
        for lesson in lessonList:
            Lesson(session).lesson_delete(lesson['id'], idMode=True)
    request.addfinalizer(fin)