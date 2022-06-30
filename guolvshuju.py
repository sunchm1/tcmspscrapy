# @author=AmiliuS

import pandas as pd
import scrapylib

INDEX='MOL_ID'
def dataFilter(herbname):
    herb=scrapylib.PDGernerator(herbname)
    ingredients=herb.ingredients
    targets=scrapylib.PDGernerator(herbname).targets
    ingredients=ingredients.loc[ingredients['ob']>=0.3].loc[ingredients['dl']>=0.18]
    targets=ingredients.merge(targets, how='left',on=INDEX)
    herb.writeFilteredData(df_ingredients=ingredients,df_targets=targets)

if __name__ == '__main__':
    formulacn=['chaihu','guizhi','ganjiang','huangqin','tianhuafen','gancao']
    for herb in formulacn:
        dataFilter(herb)

