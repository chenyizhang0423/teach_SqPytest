from lib.apiLib.login import Login
import json,pytest,os
from tools.excelMethod import get_excelData,set_excelData
from tools.getYamlData import get_yaml_data


class TestLogin:
    #@pytest.mark.parametrize('body,resData', get_excelData("1-登录接口", 2, 5))
    @pytest.mark.parametrize('body,resData', get_yaml_data())
    def test_login(self,body,resData):
        res = Login().login(body,flag=True)
        print(res)
        assert res["retcode"]==json.loads(resData)['retcode']

if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    # 方案1：直接生成报告
    # os.system('allure generate ../report/tmp -o ../report/loginReport --clean')
    # 方案2： 直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')
