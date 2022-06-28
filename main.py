# coding=utf-8
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print("Hi, {0}".format(name))  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
import scrapylib
import pandas as pd

baseurl='https://www.tcmsp-e.com/tcmspsearch.php?qr='

def getHerbData(formulacn,formulaen,token):
    '''返回GetHerbInfo对象列表'''
    herbobjects=[]
    for herbname,enname in zip(formulacn,formulaen):
        url = baseurl + enname + '&qsr=herb_en_name&token=' + token
        print(url)
        herbobject=scrapylib.GetHerbInfo(herbname,url)
        herbobjects.append(herbobject)
    return herbobjects

if __name__ == '__main__':
    '''爬取数据时调用getHerbData函数批量创建GetHerbInfo对象，数据自动写入文件。GetHerbInfo对象初始化时须传入方剂的中英文名（类型：列表）、token，返回GetHerbInfo对象列表'''

    token = '5e06333dea0727634fda8369fae7752b'
    formulacn=['chaihu','guizhi','ganjiang','huangqin','tianhuafen','gancao']
    formulaen = ['Radix%20Bupleuri', 'Cinnamomi%20Ramulus', 'Zingiberis%20Rhizoma','Scutellariae%20Radix','Trichosanthis%20Radix', 'licorice']
    #herbs=getHerbData(formulacn,formulaen,token)













    



