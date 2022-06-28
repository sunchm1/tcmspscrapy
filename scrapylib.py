import requests
import time
import random
import os
from bs4 import BeautifulSoup
import re
import json
import pandas


class GetHerbInfo:
    '''爬到的数据包装到此类，并将数据写入文件。成员变量包括成分（ingredients属性），靶点（targets属性），数据类型List'''
    def __init__(self,herbpinyinname,url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0'}
        self.herbname=herbpinyinname
        print('dealing '+self.herbname+'...')
        self.url=url
        self.response=self.getResponse(url)
        #self.saveHtml()
        self.saveScriptText()
        self.ingredients=self.getIngredients(self.herbname + '.txt')
        self.targets=self.getTargets(self.herbname + '.txt')
        self.pd_ingredients=pandas.DataFrame(self.ingredients)
        self.pd_targets=pandas.DataFrame(self.targets)
        self.writeXlsx()
        print('done...\n')

    def getResponse(self,url):
        time.sleep(random.randint(0, 5))
        r=requests.get(url,headers=self.headers)
        print("status:%s,encoding:%s"%(r.status_code,r.encoding))
        return r

    # def saveHtml(self):
    #     filename = self.herbname + '.html'
    #     html = self.response.content.decode('utf-8')
    #     if os.path.exists(filename) == False:
    #         with open(filename, 'w') as f:
    #             f.write(html)
    #     else:
    #         print("%s.html has already exists, abort saving..." % self.herbname)

    def saveScriptText(self):
        filename = self.herbname + '.txt'
        html = self.response.content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.findAll('script')
        text = scripts[11].__str__()
        if os.path.exists(filename) == False:
            with open(filename, 'w') as f:
                print('saving script text...')
                f.write(text)
        else:
            print("%s.text has already exists, abort saving..." % self.herbname)

    def getIngredients(self,filename):
        # return ingredients list (type:list)
        with open(filename,'rb') as f:
            text = f.read().decode('utf-8')
            pattern = r'\$\(\"\#grid\".*\n.*\n.*data\:\s(\[.*\])'
            repat = re.compile(pattern)
            match = repat.search(text)
            result = match.group(1)
            return json.loads(result)

    def getTargets(self,filename):
        #return targets list (type:list)
        with open(filename, 'rb') as f:
            text = f.read().decode('utf-8')
            pattern = r'\$\(\"\#grid2\".*\n.*\n.*data\:\s(\[.*\])'
            repat = re.compile(pattern)
            match = repat.search(text)
            result = match.group(1)
            return json.loads(result)

    def writeXlsx(self):
        '''将成分和靶点数据写入excel'''
        ingredientsfile = self.herbname + '_ingredients.xlsx'
        targetsfile = self.herbname + '_targets.xlsx'
        self.pd_ingredients.set_index('MOL_ID',inplace=True)
        self.pd_targets.set_index('MOL_ID',inplace=True)
        self.pd_ingredients.to_excel(ingredientsfile)
        self.pd_targets.to_excel(targetsfile)

class PDGernerator:
    def __init__(self,herbpinyinname):
        self.herbname=herbpinyinname
        self.ingredients=self.getIngredients(self.herbname + '_ingredients.xlsx')
        self.targets=self.getTargets(self.herbname + '_targets.xlsx')

    def getIngredients(self,filename):
        # return ingredients list (type:list)
        try:
            return  pandas.read_excel(filename)
        except (FileExistsError,FileNotFoundError):
            print('file not exist, create GetHerbInfo instance first')

    def getTargets(self,filename):
        #return targets list (type:list)
        try:
            return pandas.read_excel(filename)
        except (FileExistsError,FileNotFoundError):
            print('file not exist, create GetHerbInfo instance first')