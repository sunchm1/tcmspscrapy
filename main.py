# @author=AmiliuS
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













    



