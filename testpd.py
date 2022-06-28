# @author=AmiliuS

import pandas as pd
import scrapylib
s1=pd.Series([1,2,3],name='A')
s2=pd.Series([1,2,3],name='B')
df=pd.DataFrame({s1.name:s1,s2.name:s2})
print(df)
