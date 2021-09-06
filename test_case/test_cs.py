# import pytest
#
# '''
# fixture
#     scope ='function', # 级别，默认是函数。 级别有：function,class,module,session(package级别)
#     params= None,
#     autouse= False,   # 是否自动调用，设为True就是自动调用
# '''
#
#
# # @pytest.fixture()
# # def start1_func():
# #     print("----初始化操作1-----")
# # @pytest.fixture()
# # def start2_func():
# #     print("----初始化操作2-----")
# #
# # def test_01(start1_func):
# #     print("------测试test01--------")
# # def test_02(start1_func,start2_func):
# #     print("------test02--------")
#
#
# @pytest.fixture(scope='class')
# def start1_func():
#     print("----初始化操作1-----")
#
# class Test_00():
#     def test_01(self,start1_func):
#         print("测试01")
#     def test_02(self,start1_func):
#         print("测试02")
#
# class Test_01():
#     def test_03(self,start1_func):
#         print("测试03")
#     def test_04(self,start1_func):
#         print("测试04")
#
#
# if __name__ == '__main__':
#     pytest.main(['test_cs.py','-s'])
