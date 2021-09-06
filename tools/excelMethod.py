import xlrd
from xlutils.copy import copy

#1: 读取Excel数据
# 读取到的数据用列表套元祖的方式进行封装[(),().()....]
# 参数 startRow和endRow是因为一个Excel表中是一个模块的用例，一个模块中又有不同的接口用例。所以这样设计后面方便用例就扣划分
def get_excelData(sheetName,startRow,endRow,body=6,resData=8):
    resList = []
    excelDir = '../data/松勤-教管系统接口测试用例-v1.4.xls'
    workbook = xlrd.open_workbook(excelDir)
    # sheets = workbook.sheet_names()
    # 取对应的sheet来操作
    worksheet = workbook.sheet_by_name(sheetName)

    # 获取单元格 , 下标都是从0开始
    # 获取请求参数
    #worksheet.cell(1,6).value
    # 获取响应
    #worksheet.cell(1,8).value
    # 获取总行数
    # worksheet.nrows
    #return worksheet.cell(1,6).value

    for one in range(startRow-1,endRow):
        resList.append((worksheet.cell(one,body).value,worksheet.cell(one,resData).value))
    return resList

# print(get_excelData("1-登录接口",2,5))
# for one in get_excelData("1-登录接口",2,5):
#     print(one)



# 写入excel
# inData : 列表
def set_excelData(sheetIndex,startRow,endRow,column,inData,excelOutDir='../report/res.xls'):
    excelDir = '../data/松勤-教管系统接口测试用例-v1.4.xls'
    # formatting_info=True 意思是保持原格式
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)
    newWorkBook = copy(workbook)
    newWorkSheet = newWorkBook.get_sheet(sheetIndex)
    '''
    #方法一
    for one in range(startRow-1,endRow):
        newWorkSheet.write(one,column,inData[one-1])  #write(行，列，数据),  这里inDate[one-1]是因为要保证下标从0开始

    '''
    #方法二
    idx = 0
    for one in range(startRow-1,endRow):
        newWorkSheet.write(one,column,inData[idx])  #write(行，列，数据),  这里inDate[one-1]是因为要保证下标从0开始
        idx += 1

    newWorkBook.save(excelOutDir)