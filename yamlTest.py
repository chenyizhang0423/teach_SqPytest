import yaml
import json

def get_yaml_data():
    # 读取yaml文件操作，当只有一组数据时
    yamlDir = './config/test02.yaml'
    fo = open(yamlDir,"r",encoding='utf-8')
    # 使用操作库load 来加载读取文件; 文件在前
    res = yaml.load(fo,Loader = yaml.FullLoader)
    resList = []
    for one in res:
        resList.append((json.dumps(one['data']),json.dumps(one['reps'])))
    return resList
print(get_yaml_data())

# # 读取yaml文件操作，当有多组数据时
# yamlDir = './config/test.yaml'
# fo = open(yamlDir,"r",encoding='utf-8')
# # 使用操作库load 来加载读取文件; 文件在前
# res = yaml.load_all(fo,Loader = yaml.FullLoader)
# for one in res:
#     print(one)


# # 写入yaml文件操作
# yamlDir = './config/test01.yaml'
# fo = open(yamlDir,"w",encoding='utf-8')
# # runData = {'info':'normalTest'}
# runData =[1,2,3,4]
# # 注意，文件一定要放后面
# res = yaml.dump(runData,fo)
# print(res)
